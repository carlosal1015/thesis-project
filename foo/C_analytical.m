function [C] = C_analytical(x, y, t)
    mdot = 1; % kg/s
    D = 10^-3;
    L = 1;
    outer_term = mdot ./ (4 * pi * t * sqrt(D * D));
    exp_sum = 0;

    for m = -5:5

        for n = -5:5
            term1 = -(x + n * L).^2 ./ (4 * D * t);
            term2 = -(y + m * L).^2 ./ (4 * D * t);
            exp_sum = exp_sum + exp(term1 + term2);
        end

    end

    C = outer_term .* exp_sum;
end
