'''
Created on Jul 19, 2016

@author: Lee J
'''
#from lxml import html
#import requests
#from lxml.etree import XPath
#import re
#from _cffi_backend import string
from bs4 import BeautifulSoup
from urllib2 import urlopen


if __name__ == '__main__':
    
    '''define the function to get all the links for scraping the site'''
    def get_category_links(section_url):
        html = urlopen(section_url).read()
        soup = BeautifulSoup(html, "lxml")
        cats = soup.find("table", "NameCategories")
        category_links = [url + li.a["href"] for li in cats.findAll("li")]
        #print category_links
        return category_links
    
    def get_letter_link(category_link):
        html = urlopen(category_link).read()
        soup = BeautifulSoup(html, "lxml")
        cats = soup.find("table", "NameCategories")
        letter_link = [url + tr.a["href"] for tr in cats.findAll("tr", limit=1)]
        return letter_link
    
    def hack_alphabet_into_link(link, letter):
        new_link = link.replace('pha=B&s', 'pha='+str(letter)+'&s')
        return new_link
    
    def get_names_and_info(names_link_list):
        
        f = open('names_collection.txt','w')
        for link in names_link_list:
            f.write(link + '\n')
            html = urlopen(link).read()
            soup = BeautifulSoup(html, "lxml")
            cats = soup.find("table", "NameTable")
            
            try:
                
                for tr in cats.findAll("tr"):
                    f.write(str(tr))
                #go to link
                #find name info
                #copy it out write it to file
            except AttributeError as e:
                print "ain't none of them names: " + link
                
                
        f.close()
        print "done"
        return 0
    
    url = 'http://www.babynameguide.com/'
    primary_addendum = 'categories.html'
    category_links = []
    letter_links = []
    big_list = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = alphabet.upper()
    iterthing = 0 #comment later
    
    '''Go get the info about the categories of names'''
    category_links = get_category_links(url+primary_addendum)
        
    print "Category links: ", category_links
    
    #for programming use only.  Not to be used long term
    
    
    for category_link in category_links:
        letter_link = get_letter_link(category_link)
        print "Letter links: ", letter_link
        #add letter link to letter links list for later use
        letter_links.append(letter_link[0])
        '''
        if iterthing == 2:
            break #for test only.  Will comment before live go
        else:
            iterthing += 1
        '''
    print letter_links
    
    
    for link in letter_links:
        print link
        for letter, forward in zip(alphabet, alphabet[1:]):
            if letter == 'Y':
                #do stuff for Y & Z
                big_list.append(hack_alphabet_into_link(link, letter))
                big_list.append(hack_alphabet_into_link(link, forward))
                print letter, forward
            else:
                big_list.append(hack_alphabet_into_link(link, letter))
                print letter
            #add to final scraping list
    #print big_list
    
    get_names_and_info(big_list)
    
    '''
    f = open('page_info.txt','w') #opens file with this name
    
    f.write(result)
    f.close()
    '''
    #print this_page