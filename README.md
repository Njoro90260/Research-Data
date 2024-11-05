# Correlation and Regression Analysis

This repository provides a framework for analyzing correlations and linear regression between independent response variables. The code is designed to be flexible, allowing users to extend the analysis by adding additional response variables if needed.

## Features
- Correlation calculation between response datasets
- Linear regression for exploring associations between variables
- Easy-to-use scripts for expanding the analysis

## Getting Started

Follow these instructions to set up your environment and run the scripts.

### Prerequisites

1. **Python 3.6+** is recommended.
2. **Requirements file**: Make sure you have a `requirements.txt` file in the repository, which includes all necessary packages.

### Usage

1. **Set up a Virtual Environment**:
   - **For Windows**:
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```
   - **For Linux** (optional but recommended):
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

2. **Install Dependencies**:
   With the virtual environment active, install the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
3. **Run the Analysis Scripts**
   - First, execute test.py and test1.py to generate the responses data
   - If you have additional datasets, copy `test.py` as `test.py2`, `test.py3`, etc., and modify the response data as needed.
   - **Important**: Remember to import each response script (`test.py`, `test1.py`, etc.) in corelation_analysis.py to ensure all data is included in the correlation analysis.
  
  ### Adjusting the Number of Responses
  - If you want to change the number of responses used in the analysis, please take a look at the Screenshots section below for guidance on where to make these changes. (Screenshots will be added in this section for reference.)

  - **Note**: This code was tested with 300 responses per dataset. You can adjust your own response counts as required. The responses should be treated as independent variables in the analysis.

## Example Output
  - After running the correlation and regression analysis, the following outputs will be generated:
  - **Correlation matrix** for the independent variables
  - **Regression model results**(if applicable)

###Screenshots
    - Refer to this section to see where to modify the number of responses in esch script.
![counts](https://github.com/user-attachments/assets/1c562f8d-a42a-4ef8-ae95-4ebbfcde899b)
    - Change the dictionary counts to fit your response rate (in this example 100 people strongly agreed, 50 Agreed, 100 Neutral, 20 disagreed, and 0 strongly disagreed).
    - Make these changes in the `test.py`, `test1.py`, `test2.py`, etc.

![correlations](https://github.com/user-attachments/assets/e66ee879-4608-4eae-a158-337396e09976)
- Make these changes in `correlation_analysis.py`.
- **importing the data in correlation_analysis.py**
  
![importing data](https://github.com/user-attachments/assets/6567aef6-19ff-4c65-9c83-954000540d3b)


## Contributing

Contributions are welcome! If you’d like to improve this project, follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with clear messages.
4. Push your changes to your branch.
5. Open a pull request and describe the modifications.

Please ensure that your code adheres to the existing style and structure. If you’re adding a new feature, consider adding relevant tests and documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This guide should help you set up, configure, and extend the for your analysis. For any issues or additional customization, feel free to open an issue in the repository.
