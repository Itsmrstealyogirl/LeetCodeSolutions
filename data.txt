install.packages("readxl")
model_names = c("PD_SEV", "BI_SEV","PD_FRQ", "BI_FRQ")
p_vec = list(c(12), c(1), c(1,2,3), c(1,2))
p_vec_seas = list(NA,c(12),NA,NA)
d_vec = list(c(1),NA,c(12),c(1,12))
q_vec = list(c(1),NA,c(12,24), c(12))

p_coeff = list(c(-0.3432),c(-0.6122),c(0.1829, -0.0141, 0.2892),c(0.7008, 0.3897))
p_seas_coeff = list(NA,c(-0.4383),NA,NA)
q_coeff = list(c(-0.5337),c(-0.6122,-0.4383),c(-0.1989,-0.3304),c(-0.1756))

#Function for refitting the state specific model with the countrywide coefficients
#historical_dat the historical data vector containing values for Y(t-12) etc.
#model_coeff coefficients from the countrywide model to be fitted on to the state model
#champion_model the name of the champion model we're suppoesd to use
#t is the month/time variable for getting the data
countrywide_fit = function(historical_dat, model_coeff, champion_model, t) {
  yt_vec = rep(NA,length(historical_dat))
  yt_vec[13] = historical_dat$data[13]
  datvec = historical_dat$data
  starting_index = 14
  for (pred_index in seq(starting_index, length(historical_dat))) {
    yt = 0
    index = match(champion_model, model_names)
    if (is.na(index)) {
      break;
    }
    
    # adding the autoregressive terms both seasonal and non seasonal
    if(!is.na(p_vec[[index]])) {
      vec = p_vec[[index]]
      coef_vec = p_coeff[[index]]
      for (i in seq_len(length(vec))) {
        lagvec = hitorical_dat$data[historical_dat$time == (t-(i%%12))]
        term1 = lagvec[length(lagvec)]
        term2 = lagvec[length(lagvec) - 1]
        yt = yt + coef_vec[i]*(term1 - term2)
      }
      if(!is.na(p_vec_seas[[index]])) {
        vec2 = p_vec_seas[[index]]
        coef_vec2 = p_seas_coeff[[index]] 
        for (i in seq_along(vec2)) {
          lagvec = historical_dat$data[historical_dat$time == (t - (i%%12))]
          if (i%%12 == 0) {
            yt = yt + coef_vec2[i]*lagvec[length(lagvec) - (i/12)]
          }
          else {
            yt = yt + coef_vec2[i]*lagvec[length(lagvec)]
          }
        }
      }
    }
    
    # adding the differencing terms
    if(!is.na(d_vec[[index]])) {
      dvec = d_vec[[index]]
      for(i in dvec) {
        yt  = yt + lagvec[length(lagvec) - i]
      }
    }
    
    
    # adding the moving average terms
    if (!is.na(q_vec[[index]])) {
      qvec = q_vec[[index]]
      coeff_vec = q_coeff[[index]]
      for (i in qvec) {
        yt = yt + coeff_vec[i]*(datvec[pred_index - i] - yt_vec[pred_index - i])
      }
    }
    
    # adding external variables, In Progress
    
    yt_vec[pred_index] = yt
  }
  
  return (yt_vec)
}

model_vec = function(model_string) {
  # split the model passed as a string into individual characters in a list and then take the first elem of the list
  model_list = strsplit(model_string, "")
  model_list = model_list[[1]]
  
  #drop all the non numeric values in the vector and then convert vector into an integer vector
  model_list = model_list[!is.na(as.numeric(model_list))]
  model_list = as.integer(model_list)
  return (model_list)
}

data_pull = function(filename) {
  library(readxl)
  dat = read_excel(filename)
  return(dat)
}
