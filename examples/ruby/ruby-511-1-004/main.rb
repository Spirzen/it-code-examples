module BlankRefinement
  refine String do
    def blank?
      strip.empty?
    end
  end
end

class Processor
  using BlankRefinement

  def process(text)
    return if text.blank?
    text.upcase
  end
end
