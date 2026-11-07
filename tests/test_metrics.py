"""Synthetic fixtures for the recovered helper; not lab measurements."""
import unittest
from metrics.compute_kpi import compute_mttd_mttr


class MetricsTests(unittest.TestCase):
    def test_empty_has_no_measurements(self):
        self.assertEqual(compute_mttd_mttr([]), {
            "mttd_moyen_s": None, "mttr_moyen_s": None, "n_scenarios": 0,
        })

    def test_missing_boundaries_use_separate_sample_sets(self):
        # Deliberately synthetic times, unrelated to the report's measurements.
        rows = [
            {"t_attack": "2000-01-01T00:00:00+00:00",
             "t_alert": "2000-01-01T00:00:04+00:00",
             "t_remediation": "2000-01-01T00:00:06+00:00"},
            {"t_alert": "2000-01-01T00:01:00+00:00",
             "t_remediation": "2000-01-01T00:01:08+00:00"},
            {},
        ]
        self.assertEqual(compute_mttd_mttr(rows), {
            "mttd_moyen_s": 4.0, "mttr_moyen_s": 5.0, "n_scenarios": 3,
        })

    def test_timezone_offsets_refer_to_same_clock(self):
        self.assertEqual(compute_mttd_mttr([{
            "t_attack": "2000-01-01T01:00:00+01:00",
            "t_alert": "2000-01-01T00:00:07+00:00",
        }])["mttd_moyen_s"], 7.0)


if __name__ == "__main__":
    unittest.main()
