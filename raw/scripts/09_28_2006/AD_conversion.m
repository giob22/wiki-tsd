clc
clear all
close all

% Parametri della simulazione
accuracy = 1e4;                     % accuratezza della simulazione "tempo continuo"
t_i      = -30;                     % istante iniziale dell'asse dei tempi
t_f      = 30;                      % istante finale dell'asse dei tempi
D        = t_f-t_i;                 % durata dell'intervallo temporale (in secondi)
dt       = D/accuracy;              % passo della simulazione (gli altri tempi saranno multipli interi di questo)
t        = t_i:dt:t_f-dt;           % asse dei tempi
N        = length(t);               % lunghezza del vettore che definisce l'asse dei tempi
flag     = 1;                       % 1 --> Esempio 1; 2 --> Esempio 2

if flag==1
    
    %%%%%%%%%%%%%
    % Esempio 1 %
    %%%%%%%%%%%%%
    
    % Parametri del segnale
    ts_i     = -2;                      % istante iniziale del segnale s(t)
    Ds_t     = 4;                       % durata totale del segnale
    ts_i     = round(ts_i/dt)*dt;       % ridefinisce ts_i in modo che sia multiplo di dt (quindi sicuramente appartiene all'asse dei tempi da noi definito)
    ts_f     = ts_i+round(Ds_t/dt)*dt;  % istante finale del segnale s(t)
    W        = 1;                       % banda monolatera del segnale s(t)
    
    % Variabili di appoggio
    ts_l     = -1;                      % istante iniziale della parte alta del segnale
    ts_l     = round(ts_l/dt)*dt;       % ridefinisce ts_l in modo che sia multiplo di dt
    Ds       = 2;                       % durata della parte "alta" del segnale
    ts_r     = ts_l+round(Ds/dt)*dt;    % istante finale della parte "alta" del segnale s(t)
    
    % Definizione del segnale
    s = [zeros(1,length(t_i:dt:ts_i-dt)),(ts_i:dt:ts_l)+2,ones(1,length(ts_l+dt:dt:ts_r)),-(ts_r+dt:dt:ts_f-dt)+2,zeros(1,length(ts_f:dt:t_f-dt))];

else
    
    %%%%%%%%%%%%%
    % Esempio 2 %
    %%%%%%%%%%%%%
    
    % Parametri del segnale
    f0 = 4;                      % frequenza caratteristica del segnale
    W  = 4;                      % banda monolatera del segnale s(t)
    
    % Definizione del segnale
    s = 5*sin(2*pi*f0*t+pi/5)+3*sin(2*pi*(f0/3)*t+pi/8)+2*sin(2*pi*(f0/10)*t-pi/3);

end

% info   = audioinfo("Musica_1.wav") 
% [s,Fs] = audioread("Musica_1.wav");
% s = s.';
% 
% % Parametri della simulazione
% accuracy = 16000; 
% t_i      = 0;                       % istante iniziale dell'asse dei tempi
% t_f      = 1.4512;                  % istante finale dell'asse dei tempi
% D        = t_f-t_i;                 % durata dell'intervallo temporale (in secondi)
% dt       = D/accuracy;              % passo della simulazione (gli altri tempi saranno multipli interi di questo)
% t        = t_i:dt:t_f-dt;           % asse dei tempi
% N        = length(t);               % lunghezza del vettore che definisce l'asse dei tempi
% W        = 4e3;

figure
subplot(311);
plot(t,s)
xlabel('t')
ylabel('s(t)')
if flag==1
    axis([-3 3 0 1.1])   % estremi visualizzazione primo segnale
elseif flag==2
    axis([-5 5 -10 10])  % estremi visualizzazione secondo segnale
end
title('Segnale s(t)');
grid on

S_dft = fftshift(fft(s)); % algoritmo con il quale viene realizzata una DFT di un segnale (trasformata discreta di Fourier)
S     = dt*S_dft;
subplot(312);
f = linspace(-0.5,0.5,N)/dt; % asse frequenziale
plot(f,abs(S))
title('Spettro di s(t)');
grid

% Campionamento
fs = 2*W; %% utilizzando W = 1 è come se avessimo applicato un filtro anti-aliasing
Ts = 1/fs;
Ts = round(Ts/dt)*dt;                        % ridefinisce Ts in modo che sia multiplo di dt
f_samp = 1/Ts;                               % ridefinisce fs in accordo a Ts
eps   = 1e-8;                                % previene problemi di precisione numerica
high  = (abs((t/Ts)-round(t/Ts))<eps);       % individua gli istanti di campionamento
s_samp = s.*high;                            % mette a zero i valori non campionati
is    = find(high);                          % trova gli indici dei campioni
subplot(313);
stem(t(is),s_samp(is));
title('Segnale campionato');
xlabel('nT_s');
ylabel('s(nT_s )');
grid

% Scelta de filtro "pseudocontinuo" di interpolazione
% C = 1; % interpolazione costante
 C = 2; % interpolazione lineare
% C = 3; % interpolazione di Shannon

switch C
case 1
   % rect((t-Ts/2)/Ts)               % finestra rettangolare di durata Ts
   th = 0:dt:Ts;
   h  = ones(1,length(th));
case 2
   % lambda(t/Ts)                    % finestra triangolare di durata 2*Ts
   th = -Ts:dt:Ts;
   h  = 1-abs(th/Ts);
case 3
   % sinc(t/Ts)                       % sinc con lobi di durata Ts
   N_lobi  = 25;                      % in teoria ha infiniti lobi laterali, ne mettiamo 2*N_lobi
   th = -N_lobi*Ts:dt:N_lobi*Ts;
   h  = sinc(th/Ts);
end
L = length(h);


% Interpolazione
s_r       = conv(s_samp,h);                 % convoluzione
s_r_trunc = s_r(floor((L-1)/2)+1:floor((L-1)/2)+N);
% il segnale risultate da una convulozione ha una durata pari alla somma
% della durata dei segnali convoluti


figure
subplot(311);
plot(t,s_r_trunc); 
if flag==1
    axis([-3 3 0 1.1])   % estremi visualizzazione primo segnale
elseif flag==2
    axis([-5 5 -10 10])  % estremi visualizzazione secondo segnale
end
xlabel('t')
ylabel('s_r(t)')
title('Segnale ricostruito s_r(t)');
grid 

% Quantizzazione
bits  = 4;                              % numero di bit
s_min = min(s_samp);
s_max = max(s_samp);
range = s_max-s_min;                    % range di variazione del segnale campionato
Nq    = pow2(bits);                     % numero livelli di quantizzazione
Delta = range/Nq;

% ampiezza della generica cella di quantizzazione
cbook = s_min+Delta/2:Delta:s_max;      % le parole codice sono al centro delle celle

index = zeros(1,length(is));            % index conterra' gli indici delle parole codice
for k=1:length(is)
   [~,index(k)]  = min(abs(cbook-s_samp(is(k))));
end                                     
s_q = zeros(size(s_samp));                             
for k=1:length(is)
   s_q(is(k)) = cbook(index(k));      
end
subplot(312)
stem(t(is),s_q(is))
xlabel('n')
ylabel('$s_q(n)$','interpreter','latex')
title('Segnale campionato e quantizzato')
grid


% Interpolazione
sq_r       = conv(s_q,h);                 % convoluzione
sq_r_trunc = sq_r(floor((L-1)/2)+1:floor((L-1)/2)+N);
subplot(313);
plot(t,sq_r_trunc); 
if flag==1
    axis([-3 3 0 1.1])   % estremi visualizzazione primo segnale
elseif flag==2
    axis([-5 5 -10 10])  % estremi visualizzazione secondo segnale
else axis tight
end
xlabel('t')
ylabel('$\hat{s}_q(t)$','interpreter','latex')
title('Segnale ricostruito a valle del campionamento e della quantizzazione');
grid 

% Calcolo SNR di quantizzazione
P_s   = mean(s.^2);
E_q   = mean((s-sq_r_trunc).^2);
SNR_q = 10*log10(P_s/E_q) % in dB

% sound(s,Fs)
% 
% sound(sq_r_trunc,Fs)
% 

t_conv_start = t(1) + th(1);

% creo il vettore dei tempi con la stessa lunghezza del segnale
t_conv = t_conv_start + (0:(length(s_r)-1)) * dt;


