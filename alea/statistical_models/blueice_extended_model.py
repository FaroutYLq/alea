from alea.statistical_model import StatisticalModel, data
from alea.simulators import BlueiceDataGenerator
import yaml
import numpy as np
import scipy.stats as stats


class BlueiceExtendedModel(StatisticalModel):
    def __init__(self, parameter_definition: dict, ll_config: dict):
        """
        # TODO write docstring
        """
        super().__init__(parameter_definition=parameter_definition)
        self._ll = self._build_ll_from_config(ll_config)
        self.likelihood_names = [c["likelihood_term_name"] for c in ll_config]
        self.data_generators = self._build_data_generators()

        # TODO analysis_space should be inferred from the data (assert that all sources have the same analysis space)

    @classmethod
    def from_yaml(cls, yaml_file):
        with open(yaml_file, "r") as f:
            config = yaml.safe_load(f)
        return cls(**config)

    # def _ll(self, **kwargs):
    #     # TODO
    #     # IDEA Set data to blueice ll (or maybe better to set it before explicitly
    #     # since in the fit this will be called frequently but the data won't change.)
    #     # IDEA Maybe one could then define self._ll directly in the init instead of _ll_blueice?

    #     pass

    def _generate_data(self, **generate_values):
        science_data = self._generate_science_data(**generate_values)
        ancillary_measurements = self._generate_ancillary_measurements(**generate_values)
        data = np.array([(science_data, ancillary_measurements, generate_values)],
                        dtype=[('science_data', 'ancillary_measurements', 'generate_values')])
        return data

    def _generate_science_data(self, **generate_values):
        science_data = [gen.simulate(**generate_values) for gen in self.data_generators]
        return science_data

    def _generate_ancillary_measurements(self, **generate_values):
        ancillary_measurements = {}
        for name, uncertainty in self.parameters.uncertainties.items():
            param = self.parameters[name]
            if param.relative_uncertainty:
                uncertainty *= param.nominal_value  # QUESTION: Maybe rather generate_values[name]?
            if isinstance(uncertainty, float):
                parameter_meas = stats.norm(generate_values[name],
                                            uncertainty).rvs()
            else:
                # TODO: Implement str-type uncertainties
                NotImplementedError("Only float uncertainties are supported at the moment.")

            # correct parameter_meas if out of bounds
            if not param.value_in_fit_limits(parameter_meas):
                if param.fit_limits[0] is not None and parameter_meas < param.fit_limits[0]:
                    parameter_meas = param.fit_limits[0]
                elif param.fit_limits[1] is not None and parameter_meas > param.fit_limits[1]:
                    parameter_meas = param.fit_limits[1]
            ancillary_measurements[name] = parameter_meas

        return ancillary_measurements

    @data.setter
    def data(self, data):
        """
        Overrides default setter. Will also set the data of the blueice ll.
        Data-sets are expected to be in the form of a list of one or more structured arrays-- representing the data-sets of one or more likelihood terms.
        """
        # iterate through all likelihood terms and set the science data in the blueice ll
        for d, ll_term in zip(data["science_data"], self.ll.likelihood_list):
            ll_term.set_data(d)

        generate_values = data["generate_values"]
        anc_meas = data["ancillary_measurements"]
        # TODO: Set ancillary measurements for rate parameters
        # TODO: Make sure to only set each parameter once (maybe like constraint_already_set)
        # TODO: Set ancillary measurements for shape parameters

        self._data = data

    @property
    def nominal_expectation_values(self):
        # TODO
        # IDEA also enable a setter that changes the rate parameters?
        pass

    def get_expectation_values(self, **kwargs):
        # TODO
        pass

    def _build_ll_from_config(self, ll_config):
        # TODO iterate through ll_config and build blueice ll
        # IDEA Maybe simply return ll in the end and spare the def of _ll?
        # IDEA Or better define a _ll_blueice and call this in _ll to make it more readable?
        ll = None
        return ll

    def _add_rate_parameters(self):
        # TODO
        # TODO: Check if already set
        pass

    def _add_shape_parameters(self):
        # TODO
        # TODO: Check if already set
        pass

    def _build_data_generators(self):
        return [BlueiceDataGenerator(ll_term) for ll_term in self.ll.likelihood_list]
