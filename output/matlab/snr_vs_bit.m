function [b, SNR_dB, SNR_camp_dB] = snr_vs_bit(s, s_samp, is, h, n, disegna)
%SNR_VS_BIT  SNR di quantizzazione con n, n-1, ..., 1 bit e grafico con la retta a 6 dB/bit.
%
%   [b, SNR_dB, SNR_camp_dB] = snr_vs_bit(s, s_samp, is, h, n)
%   [b, SNR_dB, SNR_camp_dB] = snr_vs_bit(s, s_samp, is, h, n, false)   % senza grafico
%
%   Per ogni numero di bit b = n, n-1, ..., 1:
%     1. quantizza i campioni con un quantizzatore uniforme a 2^b livelli,
%        livelli al centro delle celle (come in AD_conversion.m);
%     2. ricostruisce il segnale: convoluzione con h e taglio di (L-1)/2 punti;
%     3. calcola l'SNR rispetto al segnale originale s.
%
%   Ingressi
%     s        segnale originale "continuo" (vettore riga, N punti)
%     s_samp   segnale campionato: uguale a s negli istanti nTs, 0 altrove (N punti)
%     is       indici dei campioni, is = find(high)
%     h        risposta impulsiva dell'interpolatore, centrata in zero (L dispari:
%              triangolo o sinc del laboratorio)
%     n        numero massimo di bit
%     disegna  (facoltativo, default true) false per non disegnare il grafico
%
%   Uscite
%     b            [n, n-1, ..., 1]
%     SNR_dB       SNR della catena completa: s contro il ricostruito  [dB]
%     SNR_camp_dB  SNR dei soli campioni: solo l'errore di quantizzazione  [dB]
%
%   Esempio, dopo aver eseguito AD_conversion.m (che definisce s, s_samp, is, h):
%     [b, snr] = snr_vs_bit(s, s_samp, is, h, 10);

if nargin < 6
    disegna = true;
end

N = length(s);
L = length(h);
a = floor((L-1)/2);                 % punti da scartare all'inizio della convoluzione

x     = s_samp(is);                 % valori dei soli campioni
x_min = min(x);                     % dinamica calcolata sui campioni
x_max = max(x);
P_s   = mean(s.^2);                 % potenza del segnale originale
P_x   = mean(x.^2);                 % potenza dei campioni

b           = n:-1:1;
SNR_dB      = zeros(size(b));
SNR_camp_dB = zeros(size(b));

for i = 1:numel(b)
    Nq    = 2^b(i);                               % numero di livelli
    Delta = (x_max - x_min)/Nq;                   % larghezza di una cella
    cbook = x_min + Delta/2 + Delta*(0:Nq-1);     % Nq livelli, al centro delle celle

    % livello più vicino = cella in cui cade il campione
    index = floor((x - x_min)/Delta) + 1;         % numero della cella (1 ... Nq)
    index = min(max(index, 1), Nq);               % x = x_max cadrebbe nella cella Nq+1
    x_q   = cbook(index);                         % campioni quantizzati

    % ricostruzione: stessa convoluzione e stesso taglio del laboratorio
    s_q        = zeros(size(s_samp));
    s_q(is)    = x_q;
    sq_r       = conv(s_q, h);
    sq_r_trunc = sq_r(a+1 : a+N);

    SNR_dB(i)      = 10*log10(P_s / mean((s - sq_r_trunc).^2));
    SNR_camp_dB(i) = 10*log10(P_x / mean((x - x_q).^2));
end

% tabella nella Command Window
fprintf('\n bit   SNR catena [dB]   SNR campioni [dB]\n');
for i = 1:numel(b)
    fprintf('%4d   %15.2f   %17.2f\n', b(i), SNR_dB(i), SNR_camp_dB(i));
end

if disegna
    % retta a 6.02 dB/bit che passa per il punto con meno bit (b = 1)
    retta = SNR_camp_dB(end) + 6.02*(b - b(end));

    figure;
    plot(b, SNR_dB, 'o-', 'LineWidth', 1.8, ...
         'DisplayName', 'SNR catena completa (s vs ricostruito)');
    hold on
    plot(b, SNR_camp_dB, 's--', 'LineWidth', 1.2, ...
         'DisplayName', 'SNR sui soli campioni (solo quantizzazione)');
    plot(b, retta, 'k:', 'LineWidth', 1.5, 'DisplayName', 'retta a 6.02 dB/bit');
    grid on
    xlabel('bit per campione');
    ylabel('SNR [dB]');
    set(gca, 'XTick', fliplr(b));
    legend('Location', 'northwest');
    title(sprintf('SNR di quantizzazione da %d a 1 bit', n));
end
end
