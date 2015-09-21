# -*- coding: utf-8 -*-
"""
Poor Man's Redirect
====================================

For changing url structures.

This plugin generates a series of html pages that redirect to the true page.
location to approximate url redirection where you don't have access to tools like .htaccess  e.g. github pages

Set ARTICLE_REDIRECT_FROM to the old format "test/{slug}/index.html"


"""


from pelican import signals
import os

def make_redirect(output_folder,redirect_from,redirect_to,relative_urls,siteurl):
    """
    produces a html file at the specified location that redirects
    
    """
    html_body = ' <!DOCTYPE html><html><head><meta \
    http-equiv="refresh" content="0; url={0}"></head><body></body></html>'

        
    file_destination = os.path.join(output_folder,redirect_from)
    
    file_path,file_name = os.path.split(file_destination)
    
    if os.path.isdir(file_path) == False:
        os.makedirs(file_path)
    
    if relative_urls:
        redirect_txt = "/" + redirect_to
    else:
        redirect_txt = siteurl + "/" + redirect_to

    html_body = html_body.format(redirect_txt)
    
    file = open(file_destination, "wb")
    file.write(html_body)
    file.close()
    
      
def create_links(generator,writer):
    for p in generator.articles:
        make_redirect(writer.output_path,p.get_url_setting('redirect_from'),p.url,writer.settings['RELATIVE_URLS'],writer.settings['SITEURL'])

def register():
    signals.article_writer_finalized.connect(create_links)
