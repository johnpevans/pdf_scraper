# Scraping Sites for PDF Documents

## Summary

This is a one-and-done program and was created to scrape certain sites for
PDFs. The program can be easily manipulated to meet the user's need.

## Requirements

The following packages/files will need to be installed.

-BeautifulSoup4
-Selenium
-chromedriver.exe

If you are using Chrome then Chromedriver.exe will need to be either installed
in the same folder as the program, or the following will need to be added to
the code:

'''
webdriver.ChromeOptions(executable_path=r"C:\FILE_PATH")
'''    

## Robots.txt
The documents I wanted to download are publicly available and in line with
their [robots.txt](https://state.nj.us/robots.txt) file. The robots.txt file
only offered restrictions on sensitive sites like Homeland Security, Department
of Banking and Insurance, Department of State, etc., but did not exclude the
Department of Human Services.

#### Methodology

I had to first look at the site and inspect the elements. It was mostly uniform
in the URL, except for those documents in 2014, so it became evident that it
would be easier to just store each of the 7 URLs in a list for the program to
loop through.

I used BeautifulSoup to scrape the links from the *href* tags in each of the
URLs, and then use Selenium to download files using the links.

I had to use try and except because I found that when the program was done it
would throw an error:

'''
Initial run received error: selenium.common.exceptions.WebDriverException:
Message: chrome not reachable
'''

I placed the message "Download complete!" to print when the error is reached.

When I initially ran the program I set the parameter for *endswith()* too
specific and as the file names were not uniform I missed a lot of the files I
wanted. I used the more general *.pdf* as it would be easier to parse out the
files I don't want after they were downloaded.

## Further Instructions and Limitations

Line 25 could be changed to ensure that the full URL is added to the list
*scraped_urls*. This will involve inspecting the elements of the web page to
see what the *href* tag has and what is missing.

For line 31 the user will need to specify the path you wish the files to be
downloaded too.

For line 32 and 42, the user will need to ensure that if they are using a
different browser, that the appropriate driver is used instead.

In the final run of the project I was able to download up to 1,066 files in
roughly 2 hours during . While downloading I noticed that one file would be
updated, replacing the prior downloaded file. The file was not important, but
if I were to make modifications to the program I would create an IF statement
to handle duplicate names or create parameters to rename the files to make them
more standardized.


## References:

https://stackoverflow.com/questions/19056031/download-files-using-requests-and-beautifulsoup

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

https://stackoverflow.com/questions/27790415/set-lxml-as-default-beautifulsoup-parser

https://stackoverflow.com/questions/40654358/how-to-control-the-download-of-files-with-selenium-python-bindings-in-chrome

## License

MIT License

Copyright (c) 2020 John P Evans

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
