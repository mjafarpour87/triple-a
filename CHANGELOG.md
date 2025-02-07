# Changelog
All notable changes to this project will be documented in this file.

## v0.0.2 - 2023-03-25
### Improvements
- Add selection-sampling
- Complete `go_affiliation_mining()` & `go_extract_topic()`
- Add Country Based Co Authorship in Jupyter Lab
- Add CLI pipeline 2023-06-15
- Manage Triple in MongoDB but not in TinyDB
- Add `get_article_pmid_list_by_cstate()` :test_tube:Not Complete
- Add `extract_triples()` in NLP services 2023-06-13
- Complete CLI config ([Issue #2](https://github.com/EhsanBitaraf/triple-a/issues/2))
- Add `get_clustering_coefficient_per_node()` ([Issue #18](https://github.com/EhsanBitaraf/triple-a/issues/18)) :test_tube:`not complete`
- Add `get_avg_shortest_path_length_per_node()` ([Issue #17](https://github.com/EhsanBitaraf/triple-a/issues/17)) :test_tube:`not complete`
- Add "time report" and "elapsed time calculation report" to the `info` function ([Issue #16](https://github.com/EhsanBitaraf/triple-a/issues/16)) .
- Add graph_diameter
- Add Graph Radius ([Issue #11](https://github.com/EhsanBitaraf/triple-a/issues/11))
    , Number of Components([Issue #14](https://github.com/EhsanBitaraf/triple-a/issues/14)) to `Info()`
- Add Citation 2023-06-06
- Improve pyproject.toml
- Add remove_duplicate in cli.export

### Bug Fixes
- Fix DOI
- Fix Security [Issue #3](https://github.com/EhsanBitaraf/triple-a/security/dependabot/3)  Bump tornado from 6.2 to 6.3.2 [#24](https://github.com/EhsanBitaraf/triple-a/pull/24)
- Fix proccess_bar in export

## v0.0.1 - 2023-02-05

### Improvements
- Build Dockerfile
- Start flake8 activity 2023-03-05
- Optional Process Bars [Issue #6](https://github.com/EhsanBitaraf/triple-a/issues/6)
- progress bar for Emmanuel function [Issue #5](https://github.com/EhsanBitaraf/triple-a/issues/5)
- add arepo cli 2023-02-26
- Improve cli
- Add graph_extract_article_cited
- Add persist.get_all_article_pmid_list , general.move_state_until , cli.triplea , cli.import
- Add gdatarefresh
- Add export_to_neo4j
- Add Visualization InteractiveGraph
- Add convert_mongodb_to_tinydb
- Restructuring project
- Add Topic Extraction
- Improve environment variables
- Add convert_db
- Add DAL Mongodb
- Add Next CLI
- Add ner_title for NER article Title
- Add ganalysis in service for graph analysing by networkx
- Add Visualization
- Improve move_state_forward
- Add Export
- Improve Service
- Improve Model
- Add get_article_by_state
- Add DAL
- Add Project Structure
- Add settings


### Bug Fixes
- Fix get_all_article_pmid_list not implemented in MongoDB [Issue #3](https://github.com/EhsanBitaraf/triple-a/issues/3)
- Fix article.Title parsing
- Fix move_state_forward
