all: talk.pdf
talk.pdf: talk.md

%.pdf: %.md
	pandoc \
		-f markdown -t beamer -o $@ \
		-V fontsize=10pt \
		--highlight-style pygments \
		--slide-level 2 \
		$<
