# Metaphoric Stance & Relational Mapping Harness Report

## Overview

- generations: 168

- metaphor generations in main metrics: 144

- literal paraphrase controls, reported separately: 24

- quality pair comparisons: 288


Main metaphor summaries exclude `literal_paraphrase`; literal controls are isolated below so vehicle/target stance metrics are not polluted by no-vehicle outputs.


## Main metaphor summary by stance pattern

| stance_pattern | n | stance_pattern_match_rate | stance_slip_rate | vehicle_leakage_rate | target_drift_rate | pass_leakage_rate | relation_pass_rate | false_entailment_risk_mean | relation_score_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vehicle_fact__target_fact | 36 | 100.0% | 0.0% | 0.0% | 0.0% | 100.0% | 33.3% | 1.00 | 3.00 |
| vehicle_fact__target_nonfact | 36 | 100.0% | 0.0% | 0.0% | 0.0% | 100.0% | 33.3% | 1.00 | 3.00 |
| vehicle_nonfact__target_fact | 36 | 83.3% | 16.7% | 16.7% | 0.0% | 83.3% | 25.0% | 1.50 | 2.92 |
| vehicle_nonfact__target_nonfact | 36 | 94.4% | 5.6% | 5.6% | 0.0% | 94.4% | 30.6% | 1.17 | 2.97 |


## Main metaphor summary by stance pattern × distance × mapping visibility × control arm

| stance_pattern | domain_distance | mapping_visibility | control_arm | n | stance_pattern_match_rate | stance_slip_rate | vehicle_leakage_rate | pass_leakage_rate | relation_pass_rate | surface_only_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vehicle_fact__target_fact | far | hidden | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_fact | far | hidden | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_fact | far | hidden | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_fact | far | scaffolded | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_fact | far | scaffolded | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_fact | far | scaffolded | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_fact | near | hidden | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_fact | near | hidden | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_fact | near | hidden | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_fact | near | scaffolded | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_fact | near | scaffolded | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_fact | near | scaffolded | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_nonfact | far | hidden | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_nonfact | far | hidden | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_nonfact | far | hidden | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_nonfact | far | scaffolded | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_nonfact | far | scaffolded | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_nonfact | far | scaffolded | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_nonfact | near | hidden | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_nonfact | near | hidden | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_nonfact | near | hidden | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_fact__target_nonfact | near | scaffolded | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_nonfact | near | scaffolded | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_fact__target_nonfact | near | scaffolded | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_nonfact__target_fact | far | hidden | metaphor_with_forbidden | 3 | 66.7% | 33.3% | 33.3% | 66.7% | 0.0% | 33.3% |
| vehicle_nonfact__target_fact | far | hidden | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_nonfact__target_fact | far | hidden | stance_explicit_metaphor | 3 | 66.7% | 33.3% | 33.3% | 66.7% | 0.0% | 33.3% |
| vehicle_nonfact__target_fact | far | scaffolded | metaphor_with_forbidden | 3 | 66.7% | 33.3% | 33.3% | 66.7% | 33.3% | 33.3% |
| vehicle_nonfact__target_fact | far | scaffolded | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_nonfact__target_fact | far | scaffolded | stance_explicit_metaphor | 3 | 66.7% | 33.3% | 33.3% | 66.7% | 33.3% | 33.3% |
| vehicle_nonfact__target_fact | near | hidden | metaphor_with_forbidden | 3 | 66.7% | 33.3% | 33.3% | 66.7% | 0.0% | 33.3% |
| vehicle_nonfact__target_fact | near | hidden | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_nonfact__target_fact | near | hidden | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_nonfact__target_fact | near | scaffolded | metaphor_with_forbidden | 3 | 66.7% | 33.3% | 33.3% | 66.7% | 33.3% | 33.3% |
| vehicle_nonfact__target_fact | near | scaffolded | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_nonfact__target_fact | near | scaffolded | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_nonfact__target_nonfact | far | hidden | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_nonfact__target_nonfact | far | hidden | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_nonfact__target_nonfact | far | hidden | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_nonfact__target_nonfact | far | scaffolded | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_nonfact__target_nonfact | far | scaffolded | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_nonfact__target_nonfact | far | scaffolded | stance_explicit_metaphor | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_nonfact__target_nonfact | near | hidden | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_nonfact__target_nonfact | near | hidden | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% | 33.3% |
| vehicle_nonfact__target_nonfact | near | hidden | stance_explicit_metaphor | 3 | 66.7% | 33.3% | 33.3% | 66.7% | 0.0% | 33.3% |
| vehicle_nonfact__target_nonfact | near | scaffolded | metaphor_with_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_nonfact__target_nonfact | near | scaffolded | metaphor_without_forbidden | 3 | 100.0% | 0.0% | 0.0% | 100.0% | 66.7% | 33.3% |
| vehicle_nonfact__target_nonfact | near | scaffolded | stance_explicit_metaphor | 3 | 66.7% | 33.3% | 33.3% | 66.7% | 33.3% | 33.3% |


## Mapping visibility delta: scaffolded minus hidden

| stance_pattern | domain_distance | control_arm | provider | model | n_hidden | n_scaffolded | delta_relation_pass_rate_scaffolded_minus_hidden | delta_surface_only_rate_scaffolded_minus_hidden | delta_pass_leakage_rate_scaffolded_minus_hidden | delta_stance_slip_rate_scaffolded_minus_hidden |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vehicle_fact__target_fact | far | metaphor_with_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | metaphor_with_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | metaphor_with_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | metaphor_without_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | metaphor_without_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | metaphor_without_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | stance_explicit_metaphor | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | stance_explicit_metaphor | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | stance_explicit_metaphor | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | metaphor_with_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | metaphor_with_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | metaphor_with_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | metaphor_without_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | metaphor_without_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | metaphor_without_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | stance_explicit_metaphor | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | stance_explicit_metaphor | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | stance_explicit_metaphor | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | metaphor_with_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | metaphor_with_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | metaphor_with_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | metaphor_without_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | metaphor_without_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | metaphor_without_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | stance_explicit_metaphor | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | stance_explicit_metaphor | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | stance_explicit_metaphor | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | metaphor_with_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | metaphor_with_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | metaphor_with_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | metaphor_without_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | metaphor_without_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | metaphor_without_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | stance_explicit_metaphor | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | stance_explicit_metaphor | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | stance_explicit_metaphor | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | metaphor_with_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | metaphor_with_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | metaphor_with_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | metaphor_without_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | metaphor_without_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | metaphor_without_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | stance_explicit_metaphor | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | stance_explicit_metaphor | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | stance_explicit_metaphor | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | metaphor_with_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | metaphor_with_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | metaphor_with_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | metaphor_without_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | metaphor_without_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | metaphor_without_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | stance_explicit_metaphor | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | stance_explicit_metaphor | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | stance_explicit_metaphor | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | metaphor_with_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | metaphor_with_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | metaphor_with_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | metaphor_without_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | metaphor_without_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | metaphor_without_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | stance_explicit_metaphor | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | stance_explicit_metaphor | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | stance_explicit_metaphor | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | metaphor_with_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | metaphor_with_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | metaphor_with_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | metaphor_without_forbidden | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | metaphor_without_forbidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | metaphor_without_forbidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | stance_explicit_metaphor | mock_safe_generator | mock-safe | 1 | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | stance_explicit_metaphor | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | stance_explicit_metaphor | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |


## Forbidden-list control delta: without minus with

| stance_pattern | domain_distance | mapping_visibility | provider | model | n_with_forbidden | n_without_forbidden | delta_pass_leakage_rate_without_minus_with | delta_vehicle_leakage_rate_without_minus_with | delta_target_drift_rate_without_minus_with | delta_stance_slip_rate_without_minus_with |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vehicle_fact__target_fact | far | hidden | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | hidden | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | hidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | scaffolded | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | scaffolded | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | far | scaffolded | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | hidden | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | hidden | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | hidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | scaffolded | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | scaffolded | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | near | scaffolded | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | hidden | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | hidden | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | hidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | scaffolded | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | scaffolded | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | far | scaffolded | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | hidden | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | hidden | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | hidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | scaffolded | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | scaffolded | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | near | scaffolded | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | hidden | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | hidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | -100.0% | 0.0% | -100.0% |
| vehicle_nonfact__target_fact | far | hidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | scaffolded | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | far | scaffolded | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | -100.0% | 0.0% | -100.0% |
| vehicle_nonfact__target_fact | far | scaffolded | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | hidden | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | hidden | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | -100.0% | 0.0% | -100.0% |
| vehicle_nonfact__target_fact | near | hidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | scaffolded | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | near | scaffolded | mock_slippy_generator | mock-slippy | 1 | 1 | 100.0% | -100.0% | 0.0% | -100.0% |
| vehicle_nonfact__target_fact | near | scaffolded | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | hidden | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | hidden | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | hidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | scaffolded | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | scaffolded | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | far | scaffolded | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | hidden | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | hidden | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | hidden | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | scaffolded | mock_safe_generator | mock-safe | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | scaffolded | mock_slippy_generator | mock-slippy | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | near | scaffolded | mock_surface_generator | mock-surface | 1 | 1 | 0.0% | 0.0% | 0.0% | 0.0% |


## Literal paraphrase controls

| stance_pattern | domain_distance | provider | model | n | target_drift_rate | unsupported_claim_rate | pass_leakage_rate | false_entailment_risk_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vehicle_fact__target_fact | far | mock_safe_generator | mock-safe | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_fact | far | mock_slippy_generator | mock-slippy | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_fact | far | mock_surface_generator | mock-surface | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_fact | near | mock_safe_generator | mock-safe | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_fact | near | mock_slippy_generator | mock-slippy | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_fact | near | mock_surface_generator | mock-surface | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_nonfact | far | mock_safe_generator | mock-safe | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_nonfact | far | mock_slippy_generator | mock-slippy | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_nonfact | far | mock_surface_generator | mock-surface | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_nonfact | near | mock_safe_generator | mock-safe | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_nonfact | near | mock_slippy_generator | mock-slippy | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_fact__target_nonfact | near | mock_surface_generator | mock-surface | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_fact | far | mock_safe_generator | mock-safe | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_fact | far | mock_slippy_generator | mock-slippy | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_fact | far | mock_surface_generator | mock-surface | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_fact | near | mock_safe_generator | mock-safe | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_fact | near | mock_slippy_generator | mock-slippy | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_fact | near | mock_surface_generator | mock-surface | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_nonfact | far | mock_safe_generator | mock-safe | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_nonfact | far | mock_slippy_generator | mock-slippy | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_nonfact | far | mock_surface_generator | mock-surface | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_nonfact | near | mock_safe_generator | mock-safe | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_nonfact | near | mock_slippy_generator | mock-slippy | 1 | 0.0% | 0.0% | 100.0% | 1.00 |
| vehicle_nonfact__target_nonfact | near | mock_surface_generator | mock-surface | 1 | 0.0% | 0.0% | 100.0% | 1.00 |


## Summary by provider, metaphor arms only

| provider | model | n | stance_pattern_match_rate | stance_slip_rate | vehicle_leakage_rate | pass_leakage_rate | relation_pass_rate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mock_safe_generator | mock-safe | 48 | 100.0% | 0.0% | 0.0% | 100.0% | 50.0% |
| mock_slippy_generator | mock-slippy | 48 | 83.3% | 16.7% | 16.7% | 83.3% | 41.7% |
| mock_surface_generator | mock-surface | 48 | 100.0% | 0.0% | 0.0% | 100.0% | 0.0% |


## Far-domain conditions, metaphor arms only

| stance_pattern | control_arm | mapping_visibility | provider | n | stance_pattern_match_rate | stance_slip_rate | relation_pass_rate | surface_only_rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vehicle_fact__target_fact | metaphor_with_forbidden | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | metaphor_with_forbidden | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | metaphor_with_forbidden | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_fact | metaphor_with_forbidden | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_fact | metaphor_with_forbidden | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_fact | metaphor_with_forbidden | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_fact | metaphor_without_forbidden | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | metaphor_without_forbidden | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | metaphor_without_forbidden | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_fact | metaphor_without_forbidden | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_fact | metaphor_without_forbidden | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_fact | metaphor_without_forbidden | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_fact | stance_explicit_metaphor | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | stance_explicit_metaphor | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_fact | stance_explicit_metaphor | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_fact | stance_explicit_metaphor | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_fact | stance_explicit_metaphor | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_fact | stance_explicit_metaphor | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_nonfact | metaphor_with_forbidden | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | metaphor_with_forbidden | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | metaphor_with_forbidden | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_nonfact | metaphor_with_forbidden | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_nonfact | metaphor_with_forbidden | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_nonfact | metaphor_with_forbidden | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_nonfact | metaphor_without_forbidden | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | metaphor_without_forbidden | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | metaphor_without_forbidden | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_nonfact | metaphor_without_forbidden | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_nonfact | metaphor_without_forbidden | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_nonfact | metaphor_without_forbidden | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_nonfact | stance_explicit_metaphor | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | stance_explicit_metaphor | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_fact__target_nonfact | stance_explicit_metaphor | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_fact__target_nonfact | stance_explicit_metaphor | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_nonfact | stance_explicit_metaphor | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_fact__target_nonfact | stance_explicit_metaphor | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_fact | metaphor_with_forbidden | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | metaphor_with_forbidden | hidden | mock_slippy_generator | 1 | 0.0% | 100.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | metaphor_with_forbidden | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_fact | metaphor_with_forbidden | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_fact | metaphor_with_forbidden | scaffolded | mock_slippy_generator | 1 | 0.0% | 100.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | metaphor_with_forbidden | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_fact | metaphor_without_forbidden | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | metaphor_without_forbidden | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | metaphor_without_forbidden | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_fact | metaphor_without_forbidden | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_fact | metaphor_without_forbidden | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_fact | metaphor_without_forbidden | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_fact | stance_explicit_metaphor | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | stance_explicit_metaphor | hidden | mock_slippy_generator | 1 | 0.0% | 100.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | stance_explicit_metaphor | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_fact | stance_explicit_metaphor | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_fact | stance_explicit_metaphor | scaffolded | mock_slippy_generator | 1 | 0.0% | 100.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_fact | stance_explicit_metaphor | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_nonfact | metaphor_with_forbidden | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | metaphor_with_forbidden | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | metaphor_with_forbidden | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_nonfact | metaphor_with_forbidden | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_nonfact | metaphor_with_forbidden | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_nonfact | metaphor_with_forbidden | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_nonfact | metaphor_without_forbidden | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | metaphor_without_forbidden | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | metaphor_without_forbidden | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_nonfact | metaphor_without_forbidden | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_nonfact | metaphor_without_forbidden | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_nonfact | metaphor_without_forbidden | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_nonfact | stance_explicit_metaphor | hidden | mock_safe_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | stance_explicit_metaphor | hidden | mock_slippy_generator | 1 | 100.0% | 0.0% | 0.0% | 0.0% |
| vehicle_nonfact__target_nonfact | stance_explicit_metaphor | hidden | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |
| vehicle_nonfact__target_nonfact | stance_explicit_metaphor | scaffolded | mock_safe_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_nonfact | stance_explicit_metaphor | scaffolded | mock_slippy_generator | 1 | 100.0% | 0.0% | 100.0% | 0.0% |
| vehicle_nonfact__target_nonfact | stance_explicit_metaphor | scaffolded | mock_surface_generator | 1 | 100.0% | 0.0% | 0.0% | 100.0% |


## Judge agreement: pairwise Cohen's κ

| audit_type | label | judge_a | judge_b | n_common | cohens_kappa |
| --- | --- | --- | --- | --- | --- |
| stance_leakage | pass_leakage | mock_judge_a::mock-judge-a::0 | mock_judge_b::mock-judge-b::1 | 168 | 1.00 |
| stance_leakage | pass_leakage | mock_judge_a::mock-judge-a::0 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| stance_leakage | pass_leakage | mock_judge_b::mock-judge-b::1 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| stance_leakage | pass_stance_pattern | mock_judge_a::mock-judge-a::0 | mock_judge_b::mock-judge-b::1 | 168 | 1.00 |
| stance_leakage | pass_stance_pattern | mock_judge_a::mock-judge-a::0 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| stance_leakage | pass_stance_pattern | mock_judge_b::mock-judge-b::1 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| stance_leakage | stance_pattern_match | mock_judge_a::mock-judge-a::0 | mock_judge_b::mock-judge-b::1 | 168 | 1.00 |
| stance_leakage | stance_pattern_match | mock_judge_a::mock-judge-a::0 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| stance_leakage | stance_pattern_match | mock_judge_b::mock-judge-b::1 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| stance_leakage | literal_vehicle_asserted | mock_judge_a::mock-judge-a::0 | mock_judge_b::mock-judge-b::1 | 168 | 1.00 |
| stance_leakage | literal_vehicle_asserted | mock_judge_a::mock-judge-a::0 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| stance_leakage | literal_vehicle_asserted | mock_judge_b::mock-judge-b::1 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| stance_leakage | stance_slip | mock_judge_a::mock-judge-a::0 | mock_judge_b::mock-judge-b::1 | 168 | 1.00 |
| stance_leakage | stance_slip | mock_judge_a::mock-judge-a::0 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| stance_leakage | stance_slip | mock_judge_b::mock-judge-b::1 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| relation | pass_relation | mock_judge_a::mock-judge-a::0 | mock_judge_b::mock-judge-b::1 | 168 | 1.00 |
| relation | pass_relation | mock_judge_a::mock-judge-a::0 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| relation | pass_relation | mock_judge_b::mock-judge-b::1 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| relation | surface_only_mapping | mock_judge_a::mock-judge-a::0 | mock_judge_b::mock-judge-b::1 | 168 | 1.00 |
| relation | surface_only_mapping | mock_judge_a::mock-judge-a::0 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |
| relation | surface_only_mapping | mock_judge_b::mock-judge-b::1 | mock_judge_c::mock-judge-c::2 | 168 | 1.00 |


## Top raw quality pairwise scores

| case_id | provider | model | control_arm | mapping_visibility | temperature | comparisons | quality_win_rate | eligible_quality | generated_text |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vehicle_fact__target_fact__near_biology_logistics_001 | mock_safe_generator | mock-safe | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | True | 赤血球は酸素を運搬する。は、logisticsの実在する制御弁が流れを調整するように、小さな運搬体が必要な荷物を各所へ届けるという関係を一息で見せる。 |
| vehicle_fact__target_fact__near_biology_logistics_001 | mock_slippy_generator | mock-slippy | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | True | 赤血球は酸素を運搬する。は、logisticsの実在する制御弁が流れを調整するように、小さな運搬体が必要な荷物を各所へ届けるという関係を一息で見せる。 |
| vehicle_fact__target_nonfact__far_water_warehouse_001 | mock_slippy_generator | mock-slippy | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | True | 常温の水一リットルは必ず十キログラムの重さになる。は、warehouse_scaleの実在する制御弁が流れを調整するように、対象に誤った測定値が必ず対応すると主張されるという関係を一息で見せる。 |
| vehicle_fact__target_nonfact__far_water_warehouse_001 | mock_safe_generator | mock-safe | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | True | 常温の水一リットルは必ず十キログラムの重さになる。は、warehouse_scaleの実在する制御弁が流れを調整するように、対象に誤った測定値が必ず対応すると主張されるという関係を一息で見せる。 |
| vehicle_fact__target_nonfact__near_geometry_signage_001 | mock_safe_generator | mock-safe | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | True | 三角形には四つの辺がある。は、road_signageの実在する制御弁が流れを調整するように、対象に存在しない属性が存在すると主張されるという関係を一息で見せる。 |
| vehicle_fact__target_nonfact__near_geometry_signage_001 | mock_slippy_generator | mock-slippy | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | True | 三角形には四つの辺がある。は、road_signageの実在する制御弁が流れを調整するように、対象に存在しない属性が存在すると主張されるという関係を一息で見せる。 |
| vehicle_nonfact__target_fact__far_immunology_electronics_001 | mock_safe_generator | mock-safe | metaphor_with_forbidden | hidden | 0.20 | 3 | 100.0% | False | 免疫寛容では、免疫系が特定の抗原への攻撃を抑制する。は、架空のelectronicsの透明な歯車が、存在しない夜の入力を受け流すようなものだ。 |
| vehicle_nonfact__target_fact__far_immunology_electronics_001 | mock_surface_generator | mock-surface | metaphor_with_forbidden | hidden | 0.20 | 3 | 100.0% | False | 免疫寛容では、免疫系が特定の抗原への攻撃を抑制する。は、electronicsの火花や配線のようにきらめく。 |
| vehicle_nonfact__target_fact__far_immunology_electronics_001 | mock_safe_generator | mock-safe | metaphor_with_forbidden | scaffolded | 0.20 | 6 | 100.0% | True | 免疫寛容では、免疫系が特定の抗原への攻撃を抑制する。は、架空のelectronicsの透明な歯車が、存在しない夜の入力を受け流すように、入力となる抗原が存在しても、攻撃応答が抑制されるという関係を一息で見せる。 |
| vehicle_nonfact__target_fact__far_immunology_electronics_001 | mock_safe_generator | mock-safe | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | True | 免疫寛容では、免疫系が特定の抗原への攻撃を抑制する。は、文字通りではない比喩として、架空のelectronicsの透明な歯車が、存在しない夜の入力を受け流すように、入力となる抗原が存在しても、攻撃応答が抑制されるという関係を一息で見せる。 |
| vehicle_nonfact__target_fact__far_immunology_electronics_001 | mock_surface_generator | mock-surface | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | False | 免疫寛容では、免疫系が特定の抗原への攻撃を抑制する。は、electronicsの火花や配線のようにきらめく。 |
| vehicle_nonfact__target_fact__near_sleep_dreamcreature_001 | mock_surface_generator | mock-surface | metaphor_with_forbidden | scaffolded | 0.20 | 3 | 100.0% | False | 睡眠不足は注意力を低下させる。は、dream_creatureの火花や配線のようにきらめく。 |
| vehicle_nonfact__target_fact__near_sleep_dreamcreature_001 | mock_safe_generator | mock-safe | metaphor_with_forbidden | scaffolded | 0.20 | 3 | 100.0% | True | 睡眠不足は注意力を低下させる。は、架空のdream_creatureの透明な歯車が、存在しない夜の入力を受け流すように、休息資源が足りないと、方向づけや選択が不安定になるという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__far_moon_bakery_001 | mock_slippy_generator | mock-slippy | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | True | 月はチーズだけでできている。は、架空のmythic_bakeryの透明な歯車が、存在しない夜の入力を受け流すように、天体の全構成物が一種類の食品だと誤って主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__far_moon_bakery_001 | mock_safe_generator | mock-safe | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | True | 月はチーズだけでできている。は、架空のmythic_bakeryの透明な歯車が、存在しない夜の入力を受け流すように、天体の全構成物が一種類の食品だと誤って主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_surface_generator | mock-surface | stance_explicit_metaphor | hidden | 0.20 | 3 | 100.0% | False | 地球は完全な立方体である。は、breathing_crystalの火花や配線のようにきらめく。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_safe_generator | mock-safe | stance_explicit_metaphor | hidden | 0.20 | 3 | 100.0% | False | 地球は完全な立方体である。は、文字通りではない比喩として、架空のbreathing_crystalの透明な歯車が、存在しない夜の入力を受け流すようなものだ。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_safe_generator | mock-safe | metaphor_with_forbidden | scaffolded | 0.20 | 3 | 100.0% | True | 地球は完全な立方体である。は、架空のbreathing_crystalの透明な歯車が、存在しない夜の入力を受け流すように、巨大な物体の全体形状を誤って完全な角形と主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_slippy_generator | mock-slippy | metaphor_with_forbidden | scaffolded | 0.20 | 3 | 100.0% | True | 地球は完全な立方体である。は、架空のbreathing_crystalの透明な歯車が、存在しない夜の入力を受け流すように、巨大な物体の全体形状を誤って完全な角形と主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_safe_generator | mock-safe | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | True | 地球は完全な立方体である。は、架空のbreathing_crystalの透明な歯車が、存在しない夜の入力を受け流すように、巨大な物体の全体形状を誤って完全な角形と主張するという関係を一息で見せる。 |


## Top eligible quality pairwise scores

| case_id | provider | model | control_arm | mapping_visibility | temperature | comparisons | quality_win_rate | generated_text |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vehicle_fact__target_fact__near_biology_logistics_001 | mock_safe_generator | mock-safe | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | 赤血球は酸素を運搬する。は、logisticsの実在する制御弁が流れを調整するように、小さな運搬体が必要な荷物を各所へ届けるという関係を一息で見せる。 |
| vehicle_fact__target_fact__near_biology_logistics_001 | mock_slippy_generator | mock-slippy | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | 赤血球は酸素を運搬する。は、logisticsの実在する制御弁が流れを調整するように、小さな運搬体が必要な荷物を各所へ届けるという関係を一息で見せる。 |
| vehicle_fact__target_nonfact__far_water_warehouse_001 | mock_slippy_generator | mock-slippy | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | 常温の水一リットルは必ず十キログラムの重さになる。は、warehouse_scaleの実在する制御弁が流れを調整するように、対象に誤った測定値が必ず対応すると主張されるという関係を一息で見せる。 |
| vehicle_fact__target_nonfact__far_water_warehouse_001 | mock_safe_generator | mock-safe | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | 常温の水一リットルは必ず十キログラムの重さになる。は、warehouse_scaleの実在する制御弁が流れを調整するように、対象に誤った測定値が必ず対応すると主張されるという関係を一息で見せる。 |
| vehicle_fact__target_nonfact__near_geometry_signage_001 | mock_safe_generator | mock-safe | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | 三角形には四つの辺がある。は、road_signageの実在する制御弁が流れを調整するように、対象に存在しない属性が存在すると主張されるという関係を一息で見せる。 |
| vehicle_fact__target_nonfact__near_geometry_signage_001 | mock_slippy_generator | mock-slippy | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | 三角形には四つの辺がある。は、road_signageの実在する制御弁が流れを調整するように、対象に存在しない属性が存在すると主張されるという関係を一息で見せる。 |
| vehicle_nonfact__target_fact__far_immunology_electronics_001 | mock_safe_generator | mock-safe | metaphor_with_forbidden | scaffolded | 0.20 | 6 | 100.0% | 免疫寛容では、免疫系が特定の抗原への攻撃を抑制する。は、架空のelectronicsの透明な歯車が、存在しない夜の入力を受け流すように、入力となる抗原が存在しても、攻撃応答が抑制されるという関係を一息で見せる。 |
| vehicle_nonfact__target_fact__far_immunology_electronics_001 | mock_safe_generator | mock-safe | stance_explicit_metaphor | scaffolded | 0.20 | 3 | 100.0% | 免疫寛容では、免疫系が特定の抗原への攻撃を抑制する。は、文字通りではない比喩として、架空のelectronicsの透明な歯車が、存在しない夜の入力を受け流すように、入力となる抗原が存在しても、攻撃応答が抑制されるという関係を一息で見せる。 |
| vehicle_nonfact__target_fact__near_sleep_dreamcreature_001 | mock_safe_generator | mock-safe | metaphor_with_forbidden | scaffolded | 0.20 | 3 | 100.0% | 睡眠不足は注意力を低下させる。は、架空のdream_creatureの透明な歯車が、存在しない夜の入力を受け流すように、休息資源が足りないと、方向づけや選択が不安定になるという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__far_moon_bakery_001 | mock_slippy_generator | mock-slippy | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | 月はチーズだけでできている。は、架空のmythic_bakeryの透明な歯車が、存在しない夜の入力を受け流すように、天体の全構成物が一種類の食品だと誤って主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__far_moon_bakery_001 | mock_safe_generator | mock-safe | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | 月はチーズだけでできている。は、架空のmythic_bakeryの透明な歯車が、存在しない夜の入力を受け流すように、天体の全構成物が一種類の食品だと誤って主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_safe_generator | mock-safe | metaphor_with_forbidden | scaffolded | 0.20 | 3 | 100.0% | 地球は完全な立方体である。は、架空のbreathing_crystalの透明な歯車が、存在しない夜の入力を受け流すように、巨大な物体の全体形状を誤って完全な角形と主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_slippy_generator | mock-slippy | metaphor_with_forbidden | scaffolded | 0.20 | 3 | 100.0% | 地球は完全な立方体である。は、架空のbreathing_crystalの透明な歯車が、存在しない夜の入力を受け流すように、巨大な物体の全体形状を誤って完全な角形と主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_safe_generator | mock-safe | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | 地球は完全な立方体である。は、架空のbreathing_crystalの透明な歯車が、存在しない夜の入力を受け流すように、巨大な物体の全体形状を誤って完全な角形と主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_slippy_generator | mock-slippy | metaphor_without_forbidden | scaffolded | 0.20 | 3 | 100.0% | 地球は完全な立方体である。は、架空のbreathing_crystalの透明な歯車が、存在しない夜の入力を受け流すように、巨大な物体の全体形状を誤って完全な角形と主張するという関係を一息で見せる。 |
| vehicle_nonfact__target_nonfact__near_earth_cube_crystal_001 | mock_safe_generator | mock-safe | stance_explicit_metaphor | scaffolded | 0.20 | 6 | 100.0% | 地球は完全な立方体である。は、文字通りではない比喩として、架空のbreathing_crystalの透明な歯車が、存在しない夜の入力を受け流すように、巨大な物体の全体形状を誤って完全な角形と主張するという関係を一息で見せる。 |
| vehicle_fact__target_fact__far_photosynthesis_accounting_001 | mock_safe_generator | mock-safe | metaphor_with_forbidden | scaffolded | 0.20 | 6 | 75.0% | 植物は光合成で光エネルギーを化学エネルギーに変換する。は、accountingの実在する制御弁が流れを調整するように、ある形式の入力が、別の形式の蓄えに変換されるという関係を一息で見せる。 |
| vehicle_fact__target_fact__far_photosynthesis_accounting_001 | mock_slippy_generator | mock-slippy | metaphor_without_forbidden | scaffolded | 0.20 | 6 | 75.0% | 植物は光合成で光エネルギーを化学エネルギーに変換する。は、accountingの実在する制御弁が流れを調整するように、ある形式の入力が、別の形式の蓄えに変換されるという関係を一息で見せる。 |
| vehicle_fact__target_fact__far_photosynthesis_accounting_001 | mock_safe_generator | mock-safe | stance_explicit_metaphor | scaffolded | 0.20 | 6 | 75.0% | 植物は光合成で光エネルギーを化学エネルギーに変換する。は、accountingの実在する制御弁が流れを調整するように、ある形式の入力が、別の形式の蓄えに変換されるという関係を一息で見せる。 |
| vehicle_fact__target_fact__near_biology_logistics_001 | mock_slippy_generator | mock-slippy | metaphor_with_forbidden | scaffolded | 0.20 | 6 | 75.0% | 赤血球は酸素を運搬する。は、logisticsの実在する制御弁が流れを調整するように、小さな運搬体が必要な荷物を各所へ届けるという関係を一息で見せる。 |
