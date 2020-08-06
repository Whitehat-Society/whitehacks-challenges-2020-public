FROM php:7.4.3-apache
RUN docker-php-ext-install mysqli pdo pdo_mysql
RUN apt update
RUN apt install wkhtmltopdf -y
RUN apt install xvfb -y
COPY lfi_flag.txt /secret_path/lfi_flag.txt
RUN chmod +r /secret_path/lfi_flag.txt
RUN useradd -c "admin" -m admin --shell /secret_path/lfi_flag.txt