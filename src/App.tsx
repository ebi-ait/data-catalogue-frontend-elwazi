import {Admin, Resource,} from "react-admin";
import {createDataProvider} from "./createDataProvider";
import {useEffect, useState} from "react";
import {DatasetList} from "./datasets";

export const App = () => {
    const [dataProvider, setDataProvider] = useState(null);
    useEffect(() => {
        const fetchDataProvider = async () => {
            const _dataProvider = await createDataProvider();
            setDataProvider(_dataProvider);
        }
        fetchDataProvider();
    }, []);

    return dataProvider
        ? (
            <Admin dataProvider={dataProvider}>
                <Resource
                    name="datasets"
                    list={DatasetList}
                />
            </Admin>
        )
        : (<div>Loading...</div>);
};