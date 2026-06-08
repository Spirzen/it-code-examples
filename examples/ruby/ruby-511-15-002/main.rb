class App < Roda
  route do |r|
    r.root do
      r.redirect '/articles'
    end

    r.on 'articles' do
      r.get Integer do |id|
        @article = Article[id]
        view('articles/show')
      end

      r.post do
        Article.create(r.params['article'])
        r.redirect
      end

      r.is do
        @articles = Article.all
        view('articles/index')
      end
    end
  end
end
