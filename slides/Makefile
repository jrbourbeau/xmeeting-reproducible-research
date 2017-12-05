all: slides.pdf
slides.pdf: slides.md

%.pdf: %.md
	pandoc \
		-f markdown -t beamer -o ../$@ \
		-V fontsize=10pt \
		--slide-level 2 \
		$<
