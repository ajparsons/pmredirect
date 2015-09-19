Poor Man's Redirect
====================================

This Pelican plugin creates an extra html file for each article that redirects to the primary page. 
This lets you change the permalink structure but preserve old links when you don't 
have access to tools like .htaccess - e.g. when building a site for github pages. 

To use add ARTICLE_REDIRECT_FROM to the settings conf.

    ARTICLE_SAVE_AS  = '{slug}/index.html'
    
    ARTICLE_REDIRECT_FROM   = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

Will generate "2015/06/05/blog-post/index.html" as a page that redirects to "blog-post/index.html"
