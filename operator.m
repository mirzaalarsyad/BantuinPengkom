x = input('Masukkan angka pertama: ');
y = input('Masukkan angka kedua: ');
op = input('Masukkan operator: ', 's');

if op == '+'
    fprintf('%d + %d = %d\n', x , y, x+y);
elseif op == '-'
    fprintf('%d - %d = %d\n', x, y, x-y);
elseif op == '/'
    fprintf('%d / %d = %d\n', x, y, floor(x/y));
elseif op == '%'
    fprintf('%d', x);
    fprintf(' %% ');
    fprintf('%d = ', y);
    fprintf('%d\n', x - y*floor(x/y)); % mod(x,y) = x - y*floor(x/y)     (gatau kenapa mod(x,y) di gua error)
end
