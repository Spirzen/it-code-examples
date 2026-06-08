require 'sidekiq'

class ReportWorker
  include Sidekiq::Worker
  sidekiq_options queue: :reports, retry: 5

  def perform(report_id)
    report = Report.find(report_id)
    report.generate_pdf!
    report.update!(status: 'ready')
  end
end

# где-то в приложении:
ReportWorker.perform_async(42)
