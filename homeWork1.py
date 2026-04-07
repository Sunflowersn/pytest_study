from selene import browser, be, have

# (опционально, но рекомендуется)
browser.config.window_width = 1280
browser.config.window_height = 800

browser.open('https://google.com')

browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()

# более стабильная проверка
browser.element('#search').should(have.text('qa.guru'))