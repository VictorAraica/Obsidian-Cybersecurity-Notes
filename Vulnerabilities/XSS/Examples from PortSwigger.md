-----------------

##  DOM XSS in `document.write` sink using source

1. Enter a random alphanumeric string into the search box.
2. Right-click and inspect the element, and observe that your random string has been placed inside an `img src` attribute.
3. Break out of the `img` attribute by searching for:
    
    `"><svg onload=alert(1)>`


------------------

##  DOM XSS in `innerHTML` sink using source `location.search`

1. Enter the following into the into the search box:
    
    `<img src=1 onerror=alert(1)>`
    
2. Click "Search".

The value of the `src` attribute is invalid and throws an error. This triggers the `onerror` event handler, which then calls the `alert()` function. As a result, the payload is executed whenever the user's browser attempts to load the page containing your malicious post.


-------------------

## DOM XSS in jQuery anchor `href` attribute sink using `location.search` source

1. On the Submit feedback page, change the query parameter `returnPath` to `/` followed by a random alphanumeric string.
2. Right-click and inspect the element, and observe that your random string has been placed inside an a `href` attribute.
3. Change `returnPath` to:
    
    `javascript:alert(document.cookie)`
    
    Hit enter and click "back".


----------------


# Reflected XSS into attribute with angle brackets HTML-encoded

1. Submit a random alphanumeric string in the search box, then use Burp Suite to intercept the search request and send it to Burp Repeater.
2. Observe that the random string has been reflected inside a quoted attribute.
3. Replace your input with the following payload to escape the quoted attribute and inject an event handler:
    
    `" onmouseover="alert(1)`
4. Verify the technique worked by right-clicking, selecting "Copy URL", and pasting the URL in the browser. When you move the mouse over the injected element it should trigger an alert.