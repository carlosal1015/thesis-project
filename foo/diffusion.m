clc
clear all

domain = -0.5:0.005:0.5;
[X, Y] = meshgrid(domain, domain);
Z = zeros(length(domain), length(domain));
cmap = hot;
cmap = flipud(cmap(:, [3 2 1]));
outfile = 'aaa.gif';
set(gcf, 'renderer', 'zbuffer');
t_vals = [0:25:100];
D = 10^-3;

for t = 1:length(t_vals)

    for i = 1:length(domain)

        for j = 1:length(domain)
            x = domain(i);
            y = domain(j);
            Z(i, j) = C_analytical(x, y, t_vals(t));
        end

    end

    hp = pcolor(X, Y, Z);
    set(hp, 'edgecolor', 'none');
    axis square;
    colormap(cmap);
    caxis manual;
    caxis([0.0 2.0]);
    hc = colorbar;
    set(get(hc, 'ylabel'), 'string', 'Concentración (kg/m^3)');
    xlabel('X (m)');
    ylabel('Y (m)');
    title(['Difusión de una fuente puntual en una caja (t=' num2str(t_vals(t)) 's)']);
    hold on;
    xlim([-0.5 0.5]);
    ylim([-0.5 0.5]);

    %    for m = -20:20
    %
    %        for n = -20:20
    %            %hcirc = circulo(n, m,  3 * sqrt(2 * D * t_vals(t)));
    %            %set(hcirc, 'color', 0.75 * ones(1, 3));
    %        end
    %
    %    end

    % gif utilities
    set(gcf, 'color', 'w');
    drawnow;
    frame = getframe(1);
    im = frame2im(frame);
    [imind, cm] = rgb2ind(im, 4096);

    if t == 1
        imwrite(imind, cm, outfile, 'gif', 'DelayTime', 0, 'loopcount', inf);
    else
        imwrite(imind, cm, outfile, 'gif', 'DelayTime', 0, 'writemode', 'append');
    end

    clf;
end
