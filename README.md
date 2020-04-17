# RegisMaster
The project is created for checking future SAT registration automatically. Simply input your username and password, and the program will do the rest for you! You will be notified once the future registration is available!

Selenium webdriver first uses the 127.0.0.1:8080 (mitmproxy) to filter out the potential detection for a webdriver, then mitmproxy forwards the request to upstream proxy to connect the Internet.

Replace "USERNAME" in "user_name.send_keys("USERNAME")" with yours.

Replace "PASSWORD" in "password.send_keys("PASSWORD")" with yours.

If you don't have mitmproxy installed, please check the following link:
https://github.com/mitmproxy/mitmproxy

Capability is indicated from the LOG file.

Sometimes the first idea might not work, but I always learn.
