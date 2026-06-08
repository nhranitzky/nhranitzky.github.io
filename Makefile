BRANCH := main
m ?= Update site

.PHONY: status commit push publish

# Arbeitsverzeichnis anzeigen
status:
	git status

# Alle Änderungen committen:  make commit m="Meine Nachricht"
commit:
	git add -A
	git commit -m "$(m)"

# Zum GitHub-Remote hochladen
push:
	git push origin $(BRANCH)

# Committen und hochladen in einem Schritt:  make publish m="Meine Nachricht"
publish: commit push
