========================
Section code explanation
========================

**page_xpath**
    is a selector for pagination. If the selector is using an endpoint, just put the endpoint with python placeholder

Example
    .. code-block:: python

        page_xpath = "https://www.99.co/id/jual/rumah?hlmn={}"

**initial_element**
    is a selector for benchmarking. If the element exists, scraper will assume that the page has successfully loaded

Example
    .. code-block:: python

        initial_element = "//h1[contains(@class, 'search-title__keyword')]"

**list_of_details_url**
    is a selector that will take all detail url to take the data later by the scraper

Example
    .. code-block:: python

        list_of_details_url = "//div[contains(@class, 'superfeatured')]/div[2]/div/div/div[2]/div/h2/a"

**max_page**
    is a variable that contains how many pages that will be scraped by the scraper

Example
    .. code-block:: python

        max_page = 2

**filename**
    is a selector that will take all detail url to take the data later by the scraper

Example
    .. code-block:: python

        filename = "scraper1.json"

**base_url**
    is a url link that ready for scraping

Example
    .. code-block:: python

        base_url = "https://www.99.co/id/jual/rumah?hlmn=1"

**Elements**
    Every element that want to be scraped by the scraper.
    Total number of elements depends on user input when set up configuration

Example

    .. code-block:: python

        image_element = "//div[contains(@class, 'galery-component__wrapper')]/img"
        price_element = "//div[contains(@class, 'property-secondary-heading__price')]/h2"
        installment_element = "//p[contains(@class, 'property-secondary-heading__installment')]/a"
        title_element = "//h1[contains(@class, 'property-secondary-heading__title')]"
        feature_element = "//ul[contains(@class, 'property-secondary-heading__feature')]"
        detail_property = "//div[contains(@class, 'property-secondary-vl__detail__column')]"
        facility_element = "//div[contains(@class, 'property-secondary__facilities__value')]"
        location_element = "//div[contains(@class, 'r123-listing-summary-v2__address')]"

