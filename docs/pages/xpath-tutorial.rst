==============
XPATH tutorial
==============

--------------
What is XPATH?
--------------
XPath is a major element in the XSLT standard. XPath can be used to navigate through elements and attributes in an XML document.

-------------------
What form is XPATH?
-------------------
.. code-block:: HTML

    <div class="ini-container-listings">
        <div class="listing">
            <h3>Listing title 1</h3>
            <div>
              <img src="https://img.com/myimg-listing1-1.jpg" />
              <img src="https://img.com/myimg-listing1-2.jpg" />
              <img src="https://img.com/myimg-listing1-3.jpg" />
            </div>
        <div>

        <div class="listing">
            <h3>Listing title 2</h3>
            <div>
              <img src="https://img.com/myimg-listing2-1.jpg" />
              <img src="https://img.com/myimg-listing2-2.jpg" />
              <img src="https://img.com/myimg-listing2-3.jpg" />
            </div>
        <div>
    </div>

-------------------------------
How to get data by using XPATH?
-------------------------------
Template selector: ``//{element}[contains(@{tag}, '{text_in_tag}')]/{next_element}/../{last_element}``

Example: how to get all images from html above
    .. code-block::

        //div[contains(@class, 'listing')]/div/img
