from unittest import TestCase

from alea.models import GaussianModel


class TestGaussianModel(TestCase):
    """Test of the Parameters class"""

    def test_gaussian_model(self):
        """Test of generate_data and fit method of the GaussianModel class"""
        parameter_definition = {
            'mu': {
                'fit_guess': 0.,
                'fittable': True,
                'nominal_value': 0.,
            },
            'sigma': {
                'fit_guess': 1.,
                'fit_limits': [
                    0.,
                    None,
                ],
                'fittable': True,
                'nominal_value': 1.,
            }
        }
        simple_model = GaussianModel(
            parameter_definition=parameter_definition)
        simple_model.data = simple_model.generate_data(mu=0, sigma=2)
        fit_result, max_llh = simple_model.fit()

        toydata_file = 'simple_data.hdf5'
        simple_model.store_data(toydata_file, [simple_model.data])
