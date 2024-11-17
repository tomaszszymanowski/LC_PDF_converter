import pymupdf

#  team_home_name = 
#  team_A_home_squad = (28, 110, 160, 363)
#  team_B_away_squad = (28, 400, 160, 630)

doc = pymupdf.open("source.pdf") # open document
page = doc[0] # get the 1st page of the document
page.set_cropbox(pymupdf.Rect(28, 50, 160, 120)) # set a cropbox for the page
doc.save("cropped-page-1.pdf")