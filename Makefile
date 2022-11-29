build:
	python -m cProfile -o out.txt dummy_app/__init__.py \
	&& gprof2dot -f pstats out.txt | dot -Tpng -o out.png
	
