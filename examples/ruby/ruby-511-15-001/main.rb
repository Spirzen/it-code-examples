require 'cuba'

Cuba.define do
  on get do
    on 'hello' do
      on param('name') do |name|
        res.write "Hello, #{name}!"
      end

      on root do
        res.redirect '/hello?name=World'
      end
    end
  end
end
