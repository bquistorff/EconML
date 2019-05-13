def TimePathGenerator(t_resids):
	leads = t_resids.keys()
	n_leads = len(leads)
	final = {}
	for lead in leads:
		new_row_group
		for lead2 in leads:
			if lead2<=lead:
				new_row_group = hstack(new_row_group, t_resids[lead2])
			else:
				new_row_group = hstack(new_row_group, np.zeros)
		final[lead] = new_row_group
	final = np.add_across_dict_add_to_index(final)
	final = demean_columns(final)

class DDML:
	def __init__(self, model_y, model_t, model_final=LinearRegression(fit_intercept=False),
                 featurizer=PolynomialFeatures(degree=1, include_bias=True),
				 treatment_generator=TimePathGenerator
                 discrete_treatment=False,
                 n_splits=2,
                 random_state=None):
		self._leads = leads
		self._dmls = {lead:DMLCateEstimator(model_y=model_y,
                         model_t=model_t,
                         model_final=model_final,
                         featurizer=featurizer,
                         discrete_treatment=discrete_treatment,
                         n_splits=n_splits,
                         random_state=random_state)
						for lead in leads}

	def fit(self, Y, T, X=None, W=None)):
		#Check for data integrity (balanced panel and same)
		y_resids, t_resids = {}, {}
		for(lead in leads):
			self._dmls[lead].fit_baseline(advance_by(Y, lead), advance_by(T, lead), X, W) #Need
			y_resids[lead], t_resids = self._dmls[lead].get_residuals() #Need
		
		Y_span = dict_concat_demean(y_resids) #y_resid+1, y_resid+2
		T_span = TimePathGenerator(t_resids)
		
		LinearRegression(Y_span, T_span, cluster=) #no const (all demeaned) 