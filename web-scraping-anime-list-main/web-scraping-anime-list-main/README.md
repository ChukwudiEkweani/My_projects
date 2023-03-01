# Web-Scraping-Anime-List
In this project, I utilized Selenium to scratch the names, evaluations, year of delivery and studio of ongoing animes from 2021 to 2022.

Selenium is an open-source programming testing system utilized for web applications. It gives a set-up of devices to mechanizing internet browsers, including Google Chrome, Mozilla Firefox, Safari, and Web Wayfarer.Cancel changes

Selenium permits engineers and analyzers to compose mechanized tests in different programming dialects, including Java, **Python**, C#, Ruby, and JavaScript. With Selenium, you can mimic client collaborations with web applications, for example, clicking buttons, finishing up structures, and exploring between pages.

Selenium comprises of a few parts, including:

Selenium WebDriver: a device for mechanizing internet browsers, which gives a programming connection point to controlling internet browsers and performing computerized testing.

Selenium IDE: a record-and-playback device for making robotized tests in Firefox.

Selenium Framework: an apparatus for running tests in lined up on different machines, which permits you to convey the tests across various programs, working frameworks, and gadgets.

Selenium is generally utilized in programming testing to work on the effectiveness and precision of experiments. It permits designers and analyzers to get bugs and mistakes prior in the advancement cycle, prompting quicker delivers and worked on quality.

Anyway in this venture, I involved selenium for webscraping despite the fact that that isn't its center plan. I utilized Selenium inpreference to BeautifulSoup due to its dynamic nature. the second justification behind utilizing selenium rather than BeutifulSoup is on the grounds that BeautifulSoup just passes html report and not powerful destinations that utilization java script and php.

The point of this venture is to exhibit the webscraping capacities of selenium and furthermore to figure out the top of the line anime shows between the year 2021 and 2022.
The venture is in two principal stages:
+ The clench hand stage is to scratch the information from <a href = "https://chia-anime.su/anime/list-mode/"> this anime site </a> utilizing Selenium.
+ The subsequent stage is to clean the scratched information utilizing the pandas library.
