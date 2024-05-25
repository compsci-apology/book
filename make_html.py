from outline import root

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Computer Scientist's Apology</title>
    <style>
        .hidden-section {
            display: none;
        }
        .see-more-button {
            cursor: pointer;
            color: blue;
            text-decoration: underline;
        }
    </style>
</head>
<body>
MAIN_CONTENT_HERE
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const seeMoreButtons = document.querySelectorAll('.see-more-button');

            seeMoreButtons.forEach(button => {
                button.addEventListener('click', function () {
                    const hiddenSection = this.previousElementSibling;
                    if (hiddenSection && hiddenSection.classList.contains('hidden-section')) {
                        hiddenSection.classList.toggle('hidden-section');
                        this.textContent = hiddenSection.classList.contains('hidden-section') ? 'See more' : 'See less';
                    } else {
                        hiddenSection.classList.add('hidden-section');
                        this.textContent = 'See more';
                    }
                });
            });
        });
    </script>
</body>
</html>
"""

if __name__ == '__main__': print(template.replace('MAIN_CONTENT_HERE', root.to_html()))
