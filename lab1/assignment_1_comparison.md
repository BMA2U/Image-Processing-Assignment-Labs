# التكليف الأول: مقارنة تفصيلية بين مكتبة OpenCV ومكتبة Pillow (PIL)

## 1. مقدمة (Introduction)
تُعدّ كلٌّ من **OpenCV** و **Pillow (PIL)** من أشهر المكتبات المتاحة في لغة بايثون للتعامل مع الصور، ولكن تُصمم كلٌّ منهما لأهداف وحالات استخدام مختلفة.

---

## 2. جدول المقارنة الشامل (Comprehensive Comparison Matrix)

| المعيار / المقارنة | مكتبة OpenCV (`cv2`) | مكتبة Pillow (`PIL`) |
| :--- | :--- | :--- |
| **الهدف الأساسي** | الرؤية الحاسوبية ومعالجة الصور المتقدمة (Computer Vision & Real-time Processing). | معالجة الصور الأساسية، التعديل، والتحويل بين الصيغ (General Image Manipulation). |
| **نظام ترتيب الألوان** | **BGR** (Blue, Green, Red) افتراضياً. | **RGB** (Red, Green, Red) افتراضياً. |
| **تمثيل بيانات الصورة** | مصفوفات **NumPy** مباشرة (`numpy.ndarray`). | كائنات اختصاصية (`PIL.Image.Image`) ويمكن تحويلها إلى NumPy. |
| **الأداء والسرعة** | فائقة السرعة، مكتوبة بلغة **C/C++** ومحسّنة للمعالجة الحية (Real-time). | سرعة ممتازة للعمليات اليومية وتعديل الأبعاد، ولكنها بطيئة في خوارزميات الرؤية الحاسوبية المعقدة. |
| **دعم الفيديو** | دعم كامل لقراءة وتعديل وتسجيل قنوات الفيديو والكاميرا الحية. | لا تدعم معالجة قنوات الفيديو المباشرة بشكل مباشر. |
| **الرسم والكتابة (Drawing)** | توفر دالّات متقدمة مثل `cv2.line`, `cv2.rectangle`, `cv2.circle`, `cv2.putText`. | تستخدم وحدة `ImageDraw` مثل `draw.line`, `draw.rectangle`, `draw.ellipse`, `draw.text`. |
| **سهولة الاستخدام** | تحتاج إلى فهم لمصفوفات الإحداثيات ونظام BGR وفتح/إغلاق النوافذ. | واجهة سهلة وبسيطة (Pythonic) وسلسة في التعامل مع الملفات والتنسيقات. |

---

## 3. الفروق الجوهرية التفصيلية

### أ. نظام ترتيب الألوان (Color Spaces)
* **OpenCV**: تقرأ الصور بنظام **BGR**. عند عرض صورة تم قراءتها بـ OpenCV باستخدام مكتبة مثل `matplotlib` سينتج اختلاف في الألوان ما لم تقم بتحويلها باستخدام:
  ```python
  img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  ```
* **Pillow**: تقرأ الصور بنظام **RGB** التلقائي المتعارف عليه في أنظمة العرض.

### ب. تمثيل البيانات (Data Representation)
* في **OpenCV**، الصورة هي عبارة عن مصفوفة أرقام من نوع `np.ndarray` بأبعاد `(Height, Width, Channels)`.
* في **Pillow**، الصورة كائن `Image` يحتوي على خصائص متعددة مثل `img.size` التي تعيد `(Width, Height)` بعكس ترتيب OpenCV.

---

## 4. مثال برمجي للمقارنة (Code Example)

### قراءة صورة وعرض حجمها:

```python
# --- باستخدام OpenCV ---
import cv2
img_cv = cv2.imread('image/network.jpg')
height, width, channels = img_cv.shape
print(f"OpenCV Shape: {height}x{width}, Channels: {channels}")

# --- باستخدام Pillow ---
from PIL import Image
img_pil = Image.open('image/network.jpg')
width, height = img_pil.size
print(f"Pillow Size: {width}x{height}, Mode: {img_pil.mode}")
```

---

## 5. الخلاصة ومتى نستخدم كل منهما؟

* **استخدم OpenCV إذا:**
  - كنت تعمل على مشاريع الرؤية الحاسوبية (Computer Vision)، مثل التعرف على الوجوه، الكشف عن الأجسام، وتتبع الحركة.
  - تتعامل مع مقاطع فيديو أو بث مباشر من الكاميرا.
  - تحتاج إلى خوارزميات معالجة صور معقدة مثل (Canny Edge, Thresholding, Contours, Filtering).

* **استخدم Pillow إذا:**
  - تحتاج إلى عمليات بسيطة مثل تغيير حجم الصورة (Resize)، قصها (Crop)، تدويرها (Rotate)، أو تغيير صيغتها (JPG to PNG).
  - تريد رسم أشكال وتصميم غلاف أو إضافة نصوص بخطوط TrueType (`.ttf`) مخصصة بسهولة.
  - تعمل في تطبيقات ويب أو معالجة دُفعية (Batch processing) سريعة للصور.
