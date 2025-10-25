# Makefile for datavalues
# Usage:
#   make build                  # local dev build -> ./dist/powerdns-$(VERSION){-py3-none-any.whl,powerdns-0.0.1.tar.gz}
#   make release VERSION=1.2-3  # full PyPi build flow
#   make clean

SHELL := bash
.ONESHELL:

# ---- Project metadata ----
PKG := datavalues
MODULE_PATH := github.com/bnassif/$(PKG)
VERSION ?= $(shell (git describe --tags --abbrev=0 2>/dev/null) || echo dev)

# ---- Paths ----
ROOT_DIR := $(abspath .)
OUT_ROOT := $(ROOT_DIR)/dist
SRC_DIR := $(ROOT_DIR)/src
PKG_DIR := $(SRC_DIR)/$(PKG)
VERSION_FILE := "$(ROOT_DIR)/src/$(PKG)/__version__.py"

# ---- Helpers ----
define need
	@command -v $(1) >/dev/null 2>&1 || { echo "ERROR: missing dependency: $(1)"; exit 1; }
endef

# ---- Default target ----
.DEFAULT_GOAL := help

.PHONY: help
help: ## Show help
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make <target> [VERSION=X]\n\nTargets:\n"} \
	/^[a-zA-Z0-9_.-]+:.*##/ { printf "  %-18s %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

# -------- Dev targets --------
.PHONY: test
test: install run_tests

.PHONY: install
install: version ## install package for local tests
	$(call need,pip)
	pip install ./

.PHONY: run_tests
run_tests: ## pytest
	$(call need,pytest)
	pytest -q

.PHONY: version
version: ## Update the version in __version__.py
	sed -i 's|__version__ *= *"[^"]*"|__version__ = "$(VERSION)"|' $(VERSION_FILE)

# -------- Release pipeline --------
.PHONY: release
release: clean build

# Step 1: prep stage dir & copy dpkg skeleton
.PHONY: clean
clean: ## Remove existing versioned stage dir
	rm -rf "$(OUT_ROOT)"
	rm -rf "$(ROOT_DIR)/.pytest_cache/"
	rm -rf "$(ROOT_DIR)/build/"
	rm -rf "$(PKG_DIR).egg-info/"
	find -type d -name "__pycache__" -exec rm -rf {} \;

.PHONY: build
build: version ## Build PyPi Package
	python -m build
