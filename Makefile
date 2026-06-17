BRANCH := main
m ?= Update site

.PHONY: status commit push publish feed

# Arbeitsverzeichnis anzeigen
status:
	git status

# feed.xml aus _data/toc.csv erzeugen
feed:
	python3 generate_feed.py

# Alle Änderungen committen:  make commit m="Meine Nachricht"
commit: feed
	git add -A
	git commit -m "$(m)"

# Zum GitHub-Remote hochladen
push:
	git push origin $(BRANCH)

# Committen und hochladen in einem Schritt:  make publish m="Meine Nachricht"
publish: commit push
