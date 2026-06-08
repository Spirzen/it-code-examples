class Drawable {
public:
    virtual void draw() const = 0;
    virtual ~Drawable() = default;
};

class Button : public Drawable { /* ... */ };

class Screen {
    std::vector<std::unique_ptr<Drawable>> widgets_;
public:
    void add(std::unique_ptr<Drawable> w) {
        widgets_.push_back(std::move(w));
    }
    void redraw() const {
        for (const auto& w : widgets_) w->draw();
    }
};
