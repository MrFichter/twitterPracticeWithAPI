##My eventual goal is writing a Python 
##program that could do customized searches, tweak the searches 
##easily, and maybe log some statistics.
##Examples of statistics might be how frequently the search 
##results hit a tweet by the same person, or how frequently a person 
##posts a tweet with a keyword in it, and what effectiveness
##rating I'd give to various searches.

##Link to main page of Twitter documentation: https://dev.twitter.com/docs/using-search

##Twitter documentation link explaining q and include_entities:
##https://dev.twitter.com/docs/api/1/get/search


##I would use this line if I were running the program in Linux: #!/usr/bin/env python

##@Fictitious suggested that the code below would be a good
##starting point.
###Next step: comb through it, see what each line does, and
###document it.
##Also see marshalBackup file.

import json
import pprint
import urllib2

def main():
  search = 'http://search.twitter.com/search.json?q=sunlightlabs&result_type=recent&include_entities=1&lang=en'
  results = json.load(urllib2.urlopen(search))['results']
  pprint.pprint(results)
  print
  print '%i results' % len(results)
  for res in results:
    print '  links in result %i:' % res['id']
    if 'entities' in res and 'urls' in res['entities']:
      for link in res['entities']['urls']:
        print '    %s' % (link.get('expanded_url') or link.get('url'))

if __name__ == '__main__':
  main()

##@Fichtitious suggests using nested dictionaries is a nice way to hang onto logs.
##You can save them to files and re-load them pretty efficiently with marshal:

