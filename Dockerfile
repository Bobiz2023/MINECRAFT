# استخدام Ubuntu كصورة أساسية
FROM ubuntu:20.04

# تثبيت المتطلبات
RUN apt-get update && apt-get install -y wget unzip curl screen python3 python3-pip

# تحميل سيرفر Minecraft Bedrock
RUN wget https://minecraft.azureedge.net/bin-linux/bedrock-server-1.20.30.02.zip \
    && unzip bedrock-server-1.20.30.02.zip -d /bedrock

# نسخ الملفات الضرورية
COPY server.py /bedrock/server.py
COPY app.py /bedrock/app.py
COPY templates /bedrock/templates
COPY static /bedrock/static

# تثبيت Flask
RUN pip3 install flask flask_basicauth

# فتح المنفذ الافتراضي لـ Minecraft Bedrock
EXPOSE 19132

# فتح المنفذ الخاص بـ Flask
EXPOSE 3000

# تعيين أمر التشغيل الافتراضي لتشغيل Flask و Minecraft
CMD ["python3", "/bedrock/app.py"]
