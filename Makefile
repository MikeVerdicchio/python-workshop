all:
	pandoc \
		-t revealjs \
		--standalone \
		--slide-level 2 \
		-V theme="verdicchio" \
		-o index.html \
		index.md