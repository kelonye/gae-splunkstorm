test:
	@$(MAKE) test --no-print-directory -C test

deps:
	@pip install -r requirements.txt

clean:
	@$(MAKE) clean -sC test

.PHONY: clean deps test
