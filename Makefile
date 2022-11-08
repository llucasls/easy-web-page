MD_FILES = $(shell ls content/)

generate:
	for file in $(MD_FILES); do\
		src/generate.py $$(echo "content/$${file}" "pages/$${file}" | sed "s/md/html/2");\
	done
