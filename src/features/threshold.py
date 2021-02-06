
class threshold:
    def threshold(num, threshold):

    if ( threshold < 0 ) || ( threshold >= 1 )
        error('threshold input must be in the range [0,1]');
    end

        fractional = num - floor( num );
        idx1 = fractional > threshold;
        idx2 = fractional <= threshold;
        difference = 1 - fractional;
        result = num + ( difference .* idx1 ) - ( fractional .* idx2 );
        return(result)
    end
