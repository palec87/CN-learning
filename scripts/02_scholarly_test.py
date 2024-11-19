import sys
sys.path.append(r"C:\Users\David Palecek\Documents\Python_projects\complex_networks\learning\scholarly")

from scholarly import scholarly, ProxyGenerator

print('import done')

# Set up a ProxyGenerator object to use free proxies
# This needs to be done only once per session
# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)

search_query = scholarly.search_author('David Palecek')
author = next(search_query)
scholarly.pprint(scholarly.fill(author, sections=['basics', 'publications']))
scholarly.pprint(author)

# # Print the titles of the author's publications
publication_titles = [pub['bib']['title'] for pub in author['publications']]
scholarly.pprint(publication_titles)

# Now search Google Scholar from behind a proxy
# search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
# scholarly.pprint(next(search_query))

# # Retrieve the author's data, fill-in, and print
# # Get an iterator for the author results
# search_query = scholarly.search_author('Steven A Cholewiak')
# # Retrieve the first result from the iterator
# first_author_result = next(search_query)
# scholarly.pprint(first_author_result)

# # Retrieve all the details for the author
# author = scholarly.fill(first_author_result )
# scholarly.pprint(author)

# # Take a closer look at the first publication
# first_publication = author['publications'][0]
# first_publication_filled = scholarly.fill(first_publication)
# scholarly.pprint(first_publication_filled)



# # Which papers cited that publication?
# citations = [citation['bib']['title'] for citation in scholarly.citedby(first_publication_filled)]
# print(citations)