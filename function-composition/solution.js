/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
	return function(x) {
      if(functions.length === 0) return x
      s = x

      for(let i = functions.length - 1; i > -1; i--){
        s = functions[i](s)
      }

      return s
    }
};
