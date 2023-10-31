import translators as ts

q_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
q_html = '''<!DOCTYPE html><html><head><title>《季姬击鸡记》</title></head><body><p>还有另一篇文章《施氏食狮史》。</p></body></html>'''

### usage
# _ = ts.preaccelerate_and_speedtest()  # Optional. Caching sessions in advance, which can help improve access speed.

print(ts.translators_pool)
print(ts.translate_text(q_text))

q_text = 'Hallo, Links'
print(ts.translate_text(q_text,translator='google',from_language='de'))
# print(ts.translate_html(q_html, translator='alibaba'))