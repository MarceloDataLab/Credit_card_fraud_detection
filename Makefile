.PHONY: lib run

lib:
	@echo "Installing libraries..."
	python3 setup.py install

run:
	@echo "Running interface..."
	python3 Credit_card_fraud_detection/interface.py


