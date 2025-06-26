"""
Composition Profiler - Flask Web Application

Vladimir Vacic
Algorithms and Computational Biology Lab
Department of Computer Science and Engineering
University of California, Riverside
Riverside, CA 92521, USA
"""

import os
import random
import string

from flask import (Flask, render_template, render_template_string, request,
                   send_file, url_for)

from cprofiler.aminoacid import AminoAcid
from cprofiler.fasta import Fasta
from cprofiler.profile import CompositionProfiler


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size


def get_header():
    return f"""
<!DOCTYPE html>
<html>
    <head>
        <title>Composition Profiler - Run</title>
        <link rel="stylesheet" href="{url_for('static', filename='css/profiler.css')}" type="text/css">
        <link rel="shortcut icon" href="{url_for('static', filename='images/icons/favicon.gif')}">
        <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    </head>
    <body>
        <table width="1000" cellpadding="0" cellspacing="6" border="0" align="center">
        <tr>
        <td align="left" valign="bottom">
            <img src="{url_for('static', filename='images/cprof.gif')}" width="167" height="41" border="0" alt="Composition Profiler logo" hspace="10" vspace="0">
        </td>
        <td align="right" valign="bottom">
            <a href="/index.html">Home</a> |
            Run Profiler |
            <a href="/examples.html">Examples</a> |
            <a href="/help.html">Help</a>
        </td>
        </tr>
    """


def get_body(query_sample,
             query_file,
             back_sample,
             back_file,
             back_source,
             back_distrib,
             alpha_value,
             bonferroni,
             iterations,
             aa_order,
             color_scheme,
             ylab,
             output_format,
             image_height,
             image_width,
             image_size_units,
             resolution):

    url_info_gif = url_for('static', filename='images/info.gif')

    html = f"""
        <form name="form" method="POST" action="/cprofiler" enctype="multipart/form-data">

        <tr>
        <td valign="top" colspan="2" align="center"">

            <table width="100%" cellpadding="0" cellspacing="3" border="0" align="center">
            <tr>
            <td colspan="2">
                <h5>Query Sample</h5>
            </td>
            </tr>
            <tr>
            <td align="right" valign="top">
                Dataset to analyze:
            </td>
            <td>
                <textarea name="query_sample" rows="8" cols="58">{query_sample}</textarea><br><br>
                Upload query sample file: <input type="file" name="query_file">
                <a href="help.html#sample"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
                <br><br>
            </td>
            </tr>
            <tr>
            <td colspan="2">
                <h6>Background Sample</h6>
            </td>
            </tr>
            <td align="right" valign="top">
                Background: <input type="radio" name="back_source" value="B" {'checked="checked"' if back_source == "B" else ''}>
            </td>
            <td>
                <textarea name="back_sample" rows="8" cols="58">{back_sample}</textarea><br><br>
                Upload background sample file: <input type="file" name="back_file">
                <a href="help.html#sample"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
                <br><br>
            </td>
            </tr>
            <tr>
            <td align="right" valign="top">
                <input type="radio" name="back_source" value="D" {'checked="checked"' if back_source == "D" else ''}>
            </td>
            <td>
                Dataset:
                <select name="back_distrib">
    """

    for key, value in CompositionProfiler.get_background_names():
        html += f"""<option value="{key}" {'selected="selected"' if key == back_distrib else ''}>{value}</option>"""

    html += f"""
                </select>
                <a href="help.html#distribution"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td colspan="2">
                <h4>Discovery and Relative Entropy Options</h4>
            </td>
            </tr>
            <tr>
            <td align="right">
                Bootstrap iterations:
            </td>
            <td>
                <select name="iterations">
                <option value="10000" selected="selected">10,000</option>
                <option value="50000">50,000</option>
                <option value="100000">100,000</option>
                </select>
                <a href="help.html#iterations"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td align="right">
                Significance (&alpha;) value:
            </td>
            <td>
                <select name="alpha_value">
                <option value="0.01">0.01</option>
                <option value="0.05" selected="selected">0.05</option>
                <option value="0.1">0.1</option>
                </select>
                <a href="help.html#alpha_value"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td align="right">
                Bonferroni correction:
            </td>
            <td>
                <input type="checkbox" name="bonferroni" value="on" checked>
                <a href="help.html#bonferroni"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td colspan="2"><br>
                <h4>Plotting Options</h4>
            </td>
            </tr>
            <tr>
            <td align="right">
                Ordering:
            </td>
            <td>
                <select name="aa_order">
    """

    for key, value in AminoAcid.get_order_names():
        html += f"""<option value="{key}" {'selected="selected"' if key == aa_order else ''}>{value}</option>"""

    html += f"""
                </select>
                <a href="help.html#order"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td align="right">
                Y-axis label:
            </td>
            <td>
                <input type="text" name="ylab" size="30" maxlength="100" value="{ylab}">
                <a href="help.html#ylab"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td align="right">
                Color scheme:
            </td>
            <td>
                <select name="color_scheme">
    """

    for key, value in AminoAcid.get_color_scheme_names():
        html += f"""<option value="{key}" {'selected="selected"' if key == color_scheme else ''}>{value}</option>"""

    html += f"""
                </select>
                <a href="help.html#color"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td align="right">
                Output format:
            </td>
            <td>
                <select name="output_format">
                <option value="png" {'selected="selected"' if output_format == 'png' else ''}>PNG (bitmap)</option>
                <option value="pdf" {'selected="selected"' if output_format == 'pdf' else ''}>PDF (vector)</option>
                <option value="eps" {'selected="selected"' if output_format == 'eps' else ''}>EPS (vector)</option>
                <option value="txt" {'selected="selected"' if output_format == 'txt' else ''}>TXT (raw values)</option>
                </select>
                <a href="help.html#format"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td align="right">
                Output size:
            </td>
            <td>
                <input type="text" name="image_width" size="6" maxlength="80" value="{image_width}"> X
                <input type="text" name="image_height" size="6" maxlength="80" value="{image_height}">
                <select name="image_size_units">
                    <option value="inch" selected="selected">inch</option>
                    <option value="cm">cm</option>
                    <option value="pixel">pixel</option>
                </select>
                <a href="help.html#size"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td align="right">
                Bitmap resolution (dpi):
            </td>
            <td>
                <input type="text" name="resolution" value="120" size="4" maxlength="8">
                <a href="help.html#resolution"><img src="{url_info_gif}" width="12" height="12" border="0"></a>
            </td>
            </tr>
            <tr>
            <td colspan="2">
                <hr noshade size="1">
                <center>
                <input type="hidden" name="command" value="create">
                <input type="submit" name="submit" value="Discover">
                <input type="submit" name="submit" value="Plot Profile">
                <input type="submit" name="submit" value="Relative Entropy">
                <input type="reset" name="reset" value="Reset">
                </center>
            </td>
            </tr>
            </table>
        </table>

        </form>

        </td>
        </tr>
    """
    return html


def get_footer():
    return """
            <tr>
            <td colspan="2"><hr noshade size="3"></td>
            </tr>
            </table>
        </body>
    </html>
    """


def print_error(message):
    return render_template_string("""
    {{ header|safe }}
    <tr><td colspan="2" align="center"><br><br><br><font color="red">Error: {{ message }}</font></td></tr>
    {{ footer|safe }}
    """, header=get_header(), footer=get_footer(), message=message)


def highlight_rows(row):
    if row['test_result'] == 'Enriched':
        return ['background-color: lightgreen'] * len(row)
    elif row['test_result'] == 'Depleted':
        return ['background-color: lightcoral'] * len(row)
    else:
        return [''] * len(row)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/examples.html')
def examples():
    return render_template('examples.html')


@app.route('/help.html')
def help():
    return render_template('help.html')


@app.route('/cprofiler', methods=['POST', 'GET'])
def profiler():
    # Get form parameters
    command = request.form.get('command', '')
    submit = request.form.get('submit', '')

    query_sample = request.form.get('query_sample', '')
    query_file = request.files.get('query_file')

    back_sample = request.form.get('back_sample', '')
    back_file = request.files.get('back_file')
    back_source = request.form.get('back_source', 'B')
    back_distrib = request.form.get('back_distrib', 'sprot')

    alpha_value = float(request.form.get('alpha_value', 0.05))
    bonferroni = request.form.get('bonferroni') == 'on'
    iterations = int(request.form.get('iterations', 10000))

    aa_order = request.form.get('aa_order', 'diff')
    color_scheme = request.form.get('color_scheme', 'mono')
    ylab = request.form.get('ylab', '')
    output_format = request.form.get('output_format', 'png')

    image_height = float(request.form.get('image_height', 3.5))
    image_width = float(request.form.get('image_width', 5))
    image_size_units = request.form.get('image_size_units', 'inch')
    resolution = int(request.form.get('resolution', 300))

    if command == "create":
        # Specify alphabet to produce data in the order in which it will be consumed
        if aa_order not in AminoAcid.list_orders():
            alphabet = AminoAcid.get_order('alpha')
        else:
            alphabet = AminoAcid.get_order(aa_order)

        # Process query data
        if query_sample:
            query = query_sample.upper().replace(' ', '').replace('\t', '')
        elif query_file and query_file.filename:
            query = query_file.read().decode('utf-8').upper().replace(' ', '').replace('\t', '')
        else:
            return print_error("Query sample missing.")

        sequences = Fasta.read_stream(query)
        if not sequences:
            return print_error("Query sample not in FastA format.")

        query_counts = Fasta.count_chars(sequences, alphabet)

        # Process background data
        if back_source == "B":
            if back_sample:
                background = back_sample.upper().replace(' ', '').replace('\t', '')
            elif back_file and back_file.filename:
                background = back_file.read().decode('utf-8').upper().replace(' ', '').replace('\t', '')
            else:
                return print_error("Background sample missing.")

            sequences = Fasta.read_stream(background)
            if not sequences:
                return print_error("Background sample not in FastA format.")

        if back_source == "D":
            sequences = Fasta.read(CompositionProfiler.get_background_file(back_distrib))

        background_counts = Fasta.count_chars(sequences, alphabet)

        #
        # Look for statistically significant composition differences between two sets
        #
        if submit == "Discover":
            try:
                if bonferroni:
                    alpha_value /= (len(alphabet) + len(AminoAcid.get_groups()))

                df = CompositionProfiler.discover(query_counts,
                                                  background_counts,
                                                  alphabet = alphabet,
                                                  groups = AminoAcid.get_groups(),
                                                  group_names = AminoAcid.get_group_names(),
                                                  iterations = iterations,
                                                  alpha_value = alpha_value)

                styled = (
                    df.style
                    .apply(highlight_rows, axis=1)
                    .hide(axis='index')
                    .set_table_attributes('border="1" cellspacing="0" cellpadding="2"')
                )

                html = styled.to_html(index=False)
                html += '''<br><p>The <a href="/help.html#references">Help</a> page contains
                        references to relevant publications.</p>'''

                return render_template_string("""
                    {{ header|safe }}
                    <tr><td colspan="2"><br><br><blockquote>{{ html|safe }}</blockquote><br></td></tr>
                    {{ footer|safe }}
                    """, header=get_header(), footer=get_footer(), html=html)

            except Exception as e:
                return print_error(f"Error in plotting a composition profile: {str(e)}")

        #
        # Draw a composition profile plot
        #
        if submit == "Plot Profile":
            try:
                output_file = f"{''.join(random.choices(string.digits, k=16))}.{output_format}"

                if image_size_units == "cm":
                    image_height /= 2.54
                    image_width /= 2.54
                elif image_size_units == "pixel":
                    image_height /= resolution
                    image_width /= resolution

                colors = []
                for ch in alphabet:
                    colors.append(AminoAcid.get_color(color_scheme, ch))

                CompositionProfiler.plot(query_counts,
                    background_counts,
                    alphabet = alphabet,
                    reorder_by_value = (aa_order == 'diff'),
                    output_format = output_format,
                    output_file = os.path.join(app.root_path, 'static', 'cache', output_file),
                    ylab = ylab,
                    colors = colors,
                    image_height = image_height,
                    image_width = image_width,
                    resolution = resolution,
                    iterations = iterations)

                if output_format == 'txt':
                    mimetype = 'text/plain'
                elif output_format == 'png':
                    mimetype = 'image/png'
                elif output_format == 'pdf':
                    mimetype = 'application/pdf'
                elif output_format == 'eps':
                    mimetype = 'application/postscript'

                return send_file(os.path.join('static', 'cache', output_file),
                                 mimetype=mimetype)

            except Exception as e:
                return print_error(f"Error in plotting a composition profile: {str(e)}")

        #
        # Computes relative entropy between two distributions of residues
        #
        if submit == "Relative Entropy":
            try:
                r, pvalue = CompositionProfiler.relent(query_counts,
                                                       background_counts,
                                                       iterations)

                html = f'Relative entropy = {r:.3f}<br>'
                if pvalue > 0:
                    html += f'P-value = {pvalue}<br>'
                else:
                    html += f'P-value < {1 / iterations}<br>'

                return render_template_string("""
                    {{ header|safe }}
                    <tr><td colspan="2"><br><br><blockquote>{{ html|safe }}</blockquote><br></td></tr>
                    {{ footer|safe }}
                    """, header=get_header(), footer=get_footer(), html=html)

            except Exception as e:
                return print_error(f"Error in computing relative entropy: {str(e)}")

    return render_template_string("""
    {{ header|safe }}
    {{ body|safe }}
    {{ footer|safe }}
    """, header=get_header(), footer=get_footer(), body=get_body(
        query_sample=query_sample,
        query_file = query_file,
        back_sample = back_sample,
        back_file = back_file,
        back_source = back_source,
        back_distrib = back_distrib,
        alpha_value = alpha_value,
        bonferroni = bonferroni,
        iterations = iterations,
        aa_order = aa_order,
        color_scheme = color_scheme,
        ylab = ylab,
        output_format = output_format,
        image_height = image_height,
        image_width = image_width,
        image_size_units = image_size_units,
        resolution = resolution)
    )


if __name__ == '__main__':
    app.run()
