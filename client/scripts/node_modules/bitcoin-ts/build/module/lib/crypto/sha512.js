import { instantiateRustWasm, sha512Base64Bytes } from '../bin/bin';
import { base64ToBin } from '../utils/utils';
/**
 * The most performant way to instantiate sha512 functionality. To avoid
 * using Node.js or DOM-specific APIs, you can use `instantiateSha512`.
 *
 * @param webassemblyBytes A buffer containing the sha512 binary.
 */
export const instantiateSha512Bytes = async (webassemblyBytes) => {
    const wasm = await instantiateRustWasm(webassemblyBytes, './sha512', 'sha512', 'sha512_init', 'sha512_update', 'sha512_final');
    return {
        final: wasm.final,
        hash: wasm.hash,
        init: wasm.init,
        update: wasm.update
    };
};
export const getEmbeddedSha512Binary = () => base64ToBin(sha512Base64Bytes).buffer;
/**
 * An ultimately-portable (but slower) version of `instantiateSha512Bytes`
 * which does not require the consumer to provide the sha512 binary buffer.
 */
export const instantiateSha512 = async () => instantiateSha512Bytes(getEmbeddedSha512Binary());
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoic2hhNTEyLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiLi4vLi4vLi4vLi4vc3JjL2xpYi9jcnlwdG8vc2hhNTEyLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBLE9BQU8sRUFFTCxtQkFBbUIsRUFDbkIsaUJBQWlCLEVBQ2xCLE1BQU0sWUFBWSxDQUFDO0FBQ3BCLE9BQU8sRUFBRSxXQUFXLEVBQUUsTUFBTSxnQkFBZ0IsQ0FBQztBQXFEN0M7Ozs7O0dBS0c7QUFDSCxNQUFNLENBQUMsTUFBTSxzQkFBc0IsR0FBRyxLQUFLLEVBQ3pDLGdCQUE2QixFQUNaLEVBQUU7SUFDbkIsTUFBTSxJQUFJLEdBQUcsTUFBTSxtQkFBbUIsQ0FDcEMsZ0JBQWdCLEVBQ2hCLFVBQVUsRUFDVixRQUFRLEVBQ1IsYUFBYSxFQUNiLGVBQWUsRUFDZixjQUFjLENBQ2YsQ0FBQztJQUNGLE9BQU87UUFDTCxLQUFLLEVBQUUsSUFBSSxDQUFDLEtBQUs7UUFDakIsSUFBSSxFQUFFLElBQUksQ0FBQyxJQUFJO1FBQ2YsSUFBSSxFQUFFLElBQUksQ0FBQyxJQUFJO1FBQ2YsTUFBTSxFQUFFLElBQUksQ0FBQyxNQUFNO0tBQ3BCLENBQUM7QUFDSixDQUFDLENBQUM7QUFFRixNQUFNLENBQUMsTUFBTSx1QkFBdUIsR0FBRyxHQUFHLEVBQUUsQ0FDMUMsV0FBVyxDQUFDLGlCQUFpQixDQUFDLENBQUMsTUFBTSxDQUFDO0FBRXhDOzs7R0FHRztBQUNILE1BQU0sQ0FBQyxNQUFNLGlCQUFpQixHQUFHLEtBQUssSUFBcUIsRUFBRSxDQUMzRCxzQkFBc0IsQ0FBQyx1QkFBdUIsRUFBRSxDQUFDLENBQUMifQ==