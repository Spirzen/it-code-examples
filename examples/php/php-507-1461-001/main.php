<?php

add_action('wp_enqueue_scripts', function () {
    $parent = 'twentytwentyfour-style';
    wp_enqueue_style($parent, get_template_directory_uri() . '/style.css');
    wp_enqueue_style(
        'ituniverse-child',
        get_stylesheet_uri(),
        [$parent],
        wp_get_theme()->get('Version')
    );
});

add_action('after_setup_theme', function () {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
});
