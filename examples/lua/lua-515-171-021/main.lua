local ReportGenerator = {}

function ReportGenerator:new()
    local gen = setmetatable({}, {__index = self})
    return gen
end

function ReportGenerator:generate(report)
    report:start()
    report:render()
    report:endReport()
end

local TextReport = {}
setmetatable(TextReport, {__index = ReportGenerator})

function TextReport:start()
    print("--- Начало текстового отчета ---")
end

function TextReport:render()
    print("Текст отчета")
end

function TextReport:endReport()
    print("--- Конец текстового отчета ---")
end

local PDFReport = {}
setmetatable(PDFReport, {__index = ReportGenerator})

function PDFReport:start()
    print("[PDF] Старт")
end

function PDFReport:render()
    print("[PDF] report body")
end

function PDFReport:endReport()
    print("[PDF] Финиш")
end

local generator = ReportGenerator:new()
generator:generate(TextReport:new())
generator:generate(PDFReport:new())
