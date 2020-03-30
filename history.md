Sourcegraph 3.14 is now available! Check out the 3.14 release blog post for more details.


repo:^github\.com/ncthuc/elastictools$ 

ncthuc/elastictools
master
HISTORY.md
# Change log

## [0.2.3] - 2019-06-19
- Fix multiple doc_type in mapping

## [0.2.2] - 2019-06-18
- Fix multiple error related to doc_type in ES7
- Update elasticsearch-py to 7.0.2
- Fix bug related to doctype while indexing document in ES 7


## [0.2.1] - 2019-06-18
- Update elasticsearch-py to 7.0.2
- Fix bug related to doctype while indexing document in ES 7

## [0.1.4] - 2018-12-07

### Added
- `DocTools.dump()`
- `DocTools.bulk_insert_from_json()`

## [0.1.3] - 2018-11-09

### Added
- `DocTools.bulk()`
- `DocTools.bulk_insert_from_csv()`
- `IndexTools.create_if_not_exists()`
- `IndexTools.truncate()`

## [0.1.2] - 2018-11-08

### Added
- `HISTORY.md`
- `long_description` in setup.py that contains content of `README.md` and `HISTORY.md`

### Changed
- `N/A`

### Removed
- `N/A`

## [0.0.1] - 2018-11-07

### Added
- `DocTools.make_search_body()`
- `DocTools.search()`
- `DocTools.msearch()`

### Changed

### Removed
