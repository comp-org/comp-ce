"use strict";

import * as yup from "yup";
import * as React from "react";
import { FormikProps } from "formik";

import {
  MetaParameters,
  MajorSection,
  LoadingElement,
  Preview,
  SectionHeaderList,
  ErrorCard
} from "./components";
import { ValidatingModal, RunModal, AuthModal } from "./modal";
import { formikToJSON, convertToFormik } from "./ParamTools";
import { hasServerErrors } from "./utils";
import {
  AccessStatus,
  Sects,
  InitialValues,
  Inputs,
  InputsDetail
} from "./types";
import API from "./API";

// need to require schema in model_parameters!
export const tbLabelSchema = yup.object().shape({
  year: yup.number(),
  MARS: yup.string(),
  idedtype: yup.string(),
  EIC: yup.string(),
  data_source: yup.string(),
  use_full_sample: yup.bool()
});


interface InputsFormProps {
  api: API;
  readOnly: boolean;
  accessStatus: AccessStatus;
  inputs: Inputs;
  defaultURL: string;

  resetInitialValues: (metaParameters: InputsDetail["meta_parameters"]) => void;
  resetting: boolean;

  formikProps: FormikProps<InitialValues>
}

interface InputsProps {
  initialValues?: InitialValues;
  sects?: Sects;
  schema?: {
    adjustment: yup.Schema<any>,
    meta_parameters: yup.Schema<any>,
    // title: yup.Schema<string>
  };
  extend?: boolean;
  unknownParams?: Array<string>;
  initialServerErrors?: { [msect: string]: { errors: { [paramName: string]: any } } };
}



const InputsForm: React.FC<InputsFormProps & InputsProps> = props => {
  if (!props.inputs || props.resetting) {
    return <LoadingElement />;
  }
  console.log("rendering InputsForm");

  let {
    accessStatus,
    inputs,

    resetInitialValues,

    schema,
    sects,
    extend,
    unknownParams,
    readOnly,
  } = props;
  let { meta_parameters, model_parameters } = inputs;
  let { sim } = inputs.detail;

  let hasUnknownParams = unknownParams.length > 0;
  let unknownParamsErrors: { [sect: string]: { errors: any } } = {
    "Unknown Parameters": { errors: {} }
  };
  if (hasUnknownParams) {
    for (const param of unknownParams) {
      unknownParamsErrors["Unknown Parameters"].errors[param] =
        "This parameter is no longer used.";
    }
  }

  let { isSubmitting, values, touched, handleSubmit, status } = props.formikProps;
  console.log(props.formikProps.values, model_parameters, meta_parameters)
  return (
    <div>
      {isSubmitting ? (
        <ValidatingModal />
      ) : (
          <div />
        )}
      {status && status.auth ? <AuthModal /> : <div />}
      <div className="row">
        <div className="col-sm-4">
          <ul className="list-unstyled components sticky-top scroll-y">
            <li>
              <MetaParameters
                meta_parameters={meta_parameters}
                values={values.meta_parameters}
                touched={touched}
                resetInitialValues={resetInitialValues}
                readOnly={props.readOnly}
              />
            </li>
            <li>
              <SectionHeaderList sects={sects} />
            </li>
            <li>
              <RunModal
                handleSubmit={handleSubmit}
                accessStatus={accessStatus}
              />
            </li>
          </ul>
        </div>
        <div className="col-sm-8">
          {status &&
            status.status === "INVALID" &&
            status.serverErrors ? (
              <ErrorCard
                errorMsg={
                  <p>
                    Some fields have errors. These must be fixed before
                    the simulation can be submitted. You may re-visit
                    this page a later time by entering the following
                            link:{" "}
                    <a href={status.editInputsUrl}>
                      {status.editInputsUrl}
                    </a>
                  </p>
                }
                errors={status.serverErrors}
                model_parameters={model_parameters}
              />
            ) : (
              <div />
            )}

          {hasUnknownParams ? (
            <ErrorCard
              errorMsg={
                <p>
                  {"One or more parameters have been renamed or " +
                    "removed since this simulation was run on " +
                    `${sim.creation_date} with version ${sim.model_version}. You may view the full simulation detail `}
                  <a href={sim.api_url}>here.</a>
                </p>
              }
              errors={unknownParamsErrors}
              model_parameters={{}}
            />
          ) : (
              <div />
            )}

          <Preview
            values={values}
            schema={yup.object().shape({
              adjustment: schema.adjustment,
              meta_parameters: schema.meta_parameters
            })}
            tbLabelSchema={tbLabelSchema}
            transformfunc={formikToJSON}
            extend={extend}
          />
          {Object.entries(sects).map((msect_item, ix) => {
            // msect --> section_1: dict(dict) --> section_2: dict(dict)
            let msect = msect_item[0];
            let section_1_dict = msect_item[1];
            return (
              <MajorSection
                key={msect}
                msect={msect}
                section_1_dict={section_1_dict}
                meta_parameters={meta_parameters}
                model_parameters={model_parameters}
                values={values}
                extend={extend}
                readOnly={readOnly}
              />
            );
          })}
        </div>
      </div>
    </div>
  );
}

const InputsMemoed = React.memo(InputsForm, (prevProps, nextProps) => {
  return (
    prevProps.accessStatus === nextProps.accessStatus &&
    prevProps.formikProps === nextProps.formikProps
  )
})
export default InputsMemoed;